import argparse
import os
import collections


def output_base_name(base, file):
    if base is None:
        out_base_name = os.path.splitext(file)[0]
    else:
        out_base_name = base
    return out_base_name


def read_input_bed(input_file):
    intervals = collections.defaultdict(list)
    with open(input_file) as input_bed:
        head = []
        for line in input_bed:
            if '#' in line or 'track' in line:
                head.append(line)
            else:
                n = len(line.split())
                chr_id, start, stop = line.split()[0:3]
                other = line.split()[3:n]
                intervals[chr_id].append((int(start), int(stop), other))
    return head, intervals


def bed_sort(intervals):
    sorted_bed = dict.fromkeys(sorted(intervals.keys()))
    for key in sorted_bed:
        sorted_bed[key] = sorted(intervals[key])
    return sorted_bed


def write_output_bed6(out_intervals, head, base):
    with open(f'{base}__output.bed', 'a') as output_bed:
        output_bed.write(''.join(head))
        for chrom in out_intervals:
            for ints in out_intervals[chrom]:
                output_bed.write(chrom + '\t' + str(ints[0]) + '\t' + str(ints[1]) + '\t' + '\t'.join(ints[2]) + '\n')
    return f'{base}__output.bed'


def write_output_bed3(out_intervals, head, base):
    with open(f'{base}__output.bed', 'a') as output_bed:
        output_bed.write(''.join(head))
        for chrom in out_intervals:
            for ints in out_intervals[chrom]:
                output_bed.write(chrom + '\t' + str(ints[0]) + '\t' + str(ints[1]) + '\n')
    return f'{base}__output.bed'


def bed_intersect(intervals_a, intervals_b):
    intersected_bed = collections.defaultdict(list)
    for chrom in intervals_a:
        if chrom in intervals_b.keys():
            for ints_a in intervals_a[chrom]:
                a = ints_a[0]
                b = ints_a[1]
                for ints_b in intervals_b[chrom]:
                    c = ints_b[0]
                    d = ints_b[1]
                    if c < b:
                        if c <= a < d:
                            intersected_bed[chrom].append((a, min(b, d)))
                        if c > a:
                            intersected_bed[chrom].append((c, min(b, d)))
                    else:
                        break
        else:
            del intersected_bed[chrom]
    return intersected_bed


parser = argparse.ArgumentParser(description='Python implementation of some bedtools functions')

parser.add_argument('-o', '--output_base_name', action='store', help='common name for output file,'
                                                                     'default: base name of input file')
parser.add_argument('--sort', action='store_true', default=False,
                    help='sort intervals by chromosome, then by start position and stop position')
parser.add_argument('-i', '--input', help='input file in BED format')
parser.add_argument('--bed6', action='store_true', default=False,
                    help='indicates that input file in BED6 format, default: False')
parser.add_argument('--intersect', action='store_true', default=False,
                    help='intersect intervals, remains positions presented in both files')
parser.add_argument('-a', help='the first file to intersect in BED format, should be sorted and merged before')
parser.add_argument('-b', help='the second file to intersect in BED format, should be sorted and merged before')


if __name__ == '__main__':
    args = vars(parser.parse_args())
    if args['sort']:
        base_name = output_base_name(args['output_base_name'], args['input'])
        header, bed_intervals = read_input_bed(args['input'])
        bed_sorted = bed_sort(bed_intervals)
        if args['bed6']:
            write_output_bed6(bed_sorted, header, (base_name + '_sorted'))
        else:
            write_output_bed3(bed_sorted, header, (base_name + '_sorted'))
    if args['intersect']:
        base_name = output_base_name(args['output_base_name'], args['a'])
        a_header, a_intervals = read_input_bed(args['a'])
        b_header, b_intervals = read_input_bed(args['b'])
        bed_intersected = bed_intersect(a_intervals, b_intervals)
        write_output_bed3(bed_intersected, (a_header + b_header), (base_name + '_intersected'))
