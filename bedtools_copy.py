import argparse
import os
import collections


def output_base_name(base, file):
    if base is None:
        out_base_name = os.path.splitext(file)[0]
    else:
        out_base_name = base
    return out_base_name


def bed_sort(intervals):
    sorted_bed = dict.fromkeys(sorted(intervals.keys()))
    for key in sorted_bed:
        sorted_bed[key] = sorted(intervals[key])
    return sorted_bed


def write_output(out_intervals, head, base):
    with open(f'{base}__output.bed', 'a') as output_bed:
        output_bed.write(''.join(head))
        for chrom in out_intervals:
            for ints in out_intervals[chrom]:
                output_bed.write(chrom + '\t' + str(ints[0]) + '\t' + str(ints[1]) + '\t' + '\t'.join(other) + '\n')
    return f'{base}__sorted.bed'


parser = argparse.ArgumentParser(description='Python implementation of some bedtools functions')
parser.add_argument('-i', '--input', help='input file(s) in BED format')
parser.add_argument('-o', '--output_base_name', action='store', help='common name for output file,'
                                                                     'default: base name of input file')
parser.add_argument('--sort', action='store_true', default=False,
                    help='sort intervals by chromosome, then by start position and stop position')

if __name__ == '__main__':
    args = vars(parser.parse_args())
    base_name = output_base_name(args['output_base_name'], args['input'])
    bed_intervals = collections.defaultdict(list)
    with open(args['input']) as input_bed:
        header = []
        for line in input_bed:
            if '#' in line or 'track' in line:
                header.append(line)
            else:
                n = len(line.split())
                chr_id, start, stop = line.split()[0:3]
                other = line.split()[3:n]
                bed_intervals[chr_id].append((int(start), int(stop), other))
    if args['sort']:
        bed_sorted = bed_sort(bed_intervals)
        write_output(bed_sorted, header, base_name)
