import argparse


def gc_content(sequence):
    gc_count = 0
    for i in range(len(sequence)):
        if sequence[i] == 'G' or sequence[i] == 'C':
            gc_count += 1
    return round(gc_count / len(sequence) * 100, 2)


parser = argparse.ArgumentParser(description='Filter .fastq files.')
parser.add_argument('--min_length', action='store',
                    type=int, help='minimal read length, integer > 0')
parser.add_argument('--keep_filtered', action='store_true', help='save failed reads')
parser.add_argument('--gc_bounds', action='append',
                    type=int, help='GC-content in %, if you want to point minimal content use it once,'
                                   'if you want to point interval, please, use this argument TWICE'
                                   'for example: --gc_content MIN --gc_content MAX')
parser.add_argument('--output_base_name', action='store', help='common name for output file(s)')
parser.add_argument('file', help='FASTQ file should be filtered')
args = parser.parse_args()


original_file = open(vars(args)['file'])
x = original_file.read().splitlines()
new_file = {}

for i in range(0, len(x), 4):
    new_file.update({x[i]: [x[i + 1], x[i + 2], x[i + 3]]})

new_file_passed_len = {}
new_file_failed = {}

for key in new_file:
    if len(new_file[key][0]) < vars(args)['min_length']:
        if vars(args)['keep_filtered']:
            new_file_failed.update({key: new_file[key]})
    else:
        new_file_passed_len.update({key: new_file[key]})

if vars(args)['gc_bounds'] is not None:
    new_file_passed_len_gc = {}
    for key in new_file_passed_len:
        if gc_content(new_file_passed_len[key][0]) < vars(args)['gc_bounds'][0]:
            if vars(args)['keep_filtered']:
                new_file_failed.update({key: new_file_passed_len[key]})
        elif len(vars(args)['gc_bounds']) == 2:
            if gc_content(new_file_passed_len[key][0]) > vars(args)['gc_bounds'][1]:
                if vars(args)['keep_filtered']:
                    new_file_failed.update({key: new_file_passed_len[key]})
            else:
                new_file_passed_len_gc.update({key: new_file_passed_len[key]})
        else:
            new_file_passed_len_gc.update({key: new_file_passed_len[key]})
    final_file_passed = new_file_passed_len_gc
else:
    final_file_passed = new_file_passed_len

if vars(args)['output_base_name'] is None:
    base_name = vars(args)['file'][:-6]
else:
    base_name = vars(args)['output_base_name']

output_passed = open(f"{base_name}__passed.fastq", 'w')
for key in final_file_passed:
    output_passed.write(key)
    output_passed.write('\n')
    output_passed.write('\n'.join(final_file_passed[key]))
    output_passed.write('\n')
output_passed.close()

if vars(args)['keep_filtered']:
    output_failed = open(f'{base_name}__failed.fastq', 'w')
    for key in new_file_failed:
        output_failed.write(key)
        output_failed.write('\n')
        output_failed.write('\n'.join(new_file_failed[key]))
        output_failed.write('\n')
    output_failed.close()

original_file.close()
