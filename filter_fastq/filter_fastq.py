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
    return f'{base}__passed.fastq'


def write_output_failed(n, s, c, q, base, keep):
    if keep:
        with open(f'{base}__failed.fastq', 'a') as output_failed:
            output_failed.write(n)
            output_failed.write(s)
            output_failed.write(c)
            output_failed.write(q)
        return f'{base}__failed.fastq'


def write_output_stats(base, dropped_length, dropped_gc):
    with open(f'{base}__stats.txt', 'a') as output_stats:
        output_stats.write(f'{dropped_length + dropped_gc} reads were dropped totally:\n')
        output_stats.write(f'{dropped_length} reads were dropped because of smaller length\n')
        output_stats.write(f'{dropped_gc} reads were dropped because of GC-content')
    return f'{base}__stats.txt'


def headcrop_function(s, q, headcrop):
    s = s[headcrop::]
    q = q[headcrop::]
    return s, q


def crop_function(s, q, crop):
    s = s[0:crop] + '\n'
    q = q[0:crop] + '\n'
    return s, q


def read_and_filter(file, length, base, keep, headcrop, crop):
    with open(file) as input_file:
        dropped_length = 0
        dropped_gc = 0
        for element in input_file:
            name = element
            seq = next(input_file)
            comment = next(input_file)
            quality = next(input_file)

            if (len(seq) - 1) < length:
                write_output_failed(name, seq, comment, quality, base, keep)
                dropped_length += 1
            else:
                if min_gc_content <= gc_content(seq) <= max_gc_content:
                    seq, quality = headcrop_function(seq, quality, headcrop)
                    if crop is not None and len(seq) - 1 > crop:
                        seq, quality = crop_function(seq, quality, crop)
                    write_output_passed(name, seq, comment, quality, base)
                else:
                    write_output_failed(name, seq, comment, quality, base, keep)
                    dropped_gc += 1
        write_output_stats(base, dropped_length, dropped_gc)


parser = argparse.ArgumentParser(description='Filter for FASTQ files')
parser.add_argument('--min_length', action='store',
                    type=int, help='minimal read length, integer > 0')
parser.add_argument('--keep_filtered', action='store_true', help='save failed reads, default: False')
parser.add_argument('--gc_bounds', nargs='+',
                    help='GC-content in %, if you want to point minimal content - point one threshold, '
                         'if you want to point interval - point two thresholds. '
                         'For example: --gc_content MIN or --gc_content MIN MAX.'
                         'If no values are pointed all reads will be passed')
parser.add_argument('-o', '--output_base_name', action='store', help='common name for output file(s),'
                                                                     'default: base name of input file')
parser.add_argument('--crop', action='store', type=int, default=None,
                    help='cut the read to a specified length')
parser.add_argument('--headcrop', action='store', type=int, default=0,
                    help='cut the specified number of bases from the start of the read, default: 0')
parser.add_argument('-file', help='FASTQ file should be filtered')


if __name__ == '__main__':
    args = vars(parser.parse_args())
    min_gc_content = gc_content_threshold(args['gc_bounds'])[0]
    max_gc_content = gc_content_threshold(args['gc_bounds'])[1]
    base_name = output_base_name(args['output_base_name'], args['file'])
    if os.path.exists(base_name + '__passed.fastq') or os.path.exists(base_name + '__failed.fastq'):
        raise FileExistsError(f'Output file already exists, remove or change output file name with -o')
    else:
        read_and_filter(args['file'], args['min_length'], base_name, args['keep_filtered'], args['headcrop'],
                        args['crop'])
