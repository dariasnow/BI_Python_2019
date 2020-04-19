import argparse
import os


def gc_content(sequence):
    gc_count = 0
    if len(sequence) == 0:
        return 0
    else:
        for i in range(len(sequence)):
            if sequence[i] == 'G' or sequence[i] == 'C':
                gc_count += 1
        return round(gc_count / len(sequence) * 100, 2)


def gc_content_threshold(arg):
    if arg is None:
        min_gc = 0
        max_gc = 100
    elif len(arg) == 1:
        min_gc = int(arg[0])
        max_gc = 100
    else:
        min_gc = int(arg[0])
        max_gc = int(arg[1])
    return [min_gc, max_gc]


def output_base_name(base, file):
    if base is None:
        out_base_name = os.path.splitext(file)[0]
    else:
        out_base_name = base
    return out_base_name


def write_output_passed(n, s, c, q, base):
    with open(f'{base}__passed.fastq', 'a') as output_passed:
        output_passed.write(n)
        output_passed.write(s)
        output_passed.write(c)
        output_passed.write(q)
    return output_passed


def write_output_failed(n, s, c, q, base, keep):
    if keep:
        with open(f'{base}__failed.fastq', 'a') as output_failed:
            output_failed.write(n)
            output_failed.write(s)
            output_failed.write(c)
            output_failed.write(q)
        return f'{base}__failed.fastq'


def read_and_filter(file, length, base, keep):
    with open(file) as input_file:
        for element in input_file:
            name = element
            seq = next(input_file)
            comment = next(input_file)
            quality = next(input_file)

            if (len(seq) - 1) < length:
                write_output_failed(name, seq, comment, quality, base, keep)
            else:
                if min_gc_content <= gc_content(seq) <= max_gc_content:
                    write_output_passed(name, seq, comment, quality, base)
                else:
                    write_output_failed(name, seq, comment, quality, base, keep)


parser = argparse.ArgumentParser(description='Filter for FASTQ files')
parser.add_argument('--min_length', action='store',
                    type=int, help='minimal read length, integer > 0')
parser.add_argument('--keep_filtered', action='store_true', help='save failed reads, default: False')
parser.add_argument('--gc_bounds', nargs='+',
                    help='GC-content in %, if you want to point minimal content - point one threshold, '
                         'if you want to point interval - point two thresholds. '
                         'For example: --gc_content MIN or --gc_content MIN MAX.'
                         'If no values are pointed all reads will be passed')
parser.add_argument('-o', '--output_base_name', action='store', help='common name for output file(s)')
parser.add_argument('-file', help='FASTQ file should be filtered')


if __name__ == '__main__':
    args = vars(parser.parse_args())
    min_gc_content = gc_content_threshold(args['gc_bounds'])[0]
    max_gc_content = gc_content_threshold(args['gc_bounds'])[1]
    base_name = output_base_name(args['output_base_name'], args['file'])
    if os.path.exists(base_name + '__passed.fastq'):
        raise FileExistsError(f'Output file {base_name}__passed.fastq already exists, '
                              f'remove or change output file name with -o')
    else:
        read_and_filter(args['file'], args['min_length'], base_name, args['keep_filtered'])
