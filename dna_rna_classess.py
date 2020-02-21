class Dna:
    def __init__(self, sequence):
        self.sequence = sequence
        self.error = 0

    def gc_content(self):
        gc_count = 0
        for i in range(len(self.sequence)):
            if self.sequence[i] == 'G' or self.sequence[i] == 'C':
                gc_count += 1
            elif self.sequence[i] == 'A' or self.sequence[i] == 'T':
                gc_count += 0
            else:
                print('Incorrect type or sequence!')
                self.error += 1
                break
        if self.error == 0:
            self.gc_content = round(gc_count / len(self.sequence) * 100, 2)


    def reverse_complement(self):
        reverse_sequence = [0] * len(self.sequence)
        for i in range(len(self.sequence)):
            if self.sequence[i] == 'A':
                reverse_sequence[i] = 'T'
            elif self.sequence[i] == 'T':
                reverse_sequence[i] = 'A'
            elif self.sequence[i] == 'G':
                reverse_sequence[i] = 'C'
            elif self.sequence[i] == 'C':
                reverse_sequence[i] = 'G'
            else:
                print('Incorrect type or sequence!')
                self.error += 1
                break
        if self.error == 0:
            self.reverse_complement = ''.join(reverse_sequence)

    def transcribe(self):
        transcript_seq = [0] * len(self.sequence)
        for i in range(len(self.sequence)):
            if self.sequence[i] == 'A':
                transcript_seq[i] = 'U'
            elif self.sequence[i] == 'T':
                transcript_seq[i] = 'A'
            elif self.sequence[i] == 'G':
                transcript_seq[i] = 'C'
            elif self.sequence[i] == 'C':
                transcript_seq[i] = 'G'
            else:
                print('Incorrect type or sequence!')
                self.error += 1
                break
        if self.error == 0:
            self.transcribe = ''.join(transcript_seq)
            # I don't know how to make object of Rna


class Rna:
    def __init__(self, sequence):
        self.sequence = sequence
        self.error = 0

    def gc_content(self):
        gc_count = 0
        for i in range(len(self.sequence)):
            if self.sequence[i] == 'G' or self.sequence[i] == 'C':
                gc_count += 1
            elif self.sequence[i] == 'A' or self.sequence[i] == 'U':
                gc_count += 0
            else:
                print('Incorrect type or sequence!')
                self.error += 1
                break
        if self.error == 0:
            self.gc_content = round(gc_count / len(self.sequence) * 100, 2)


    def reverse_complement(self):
        pass
        reverse_sequence = [0] * len(self.sequence)
        for i in range(len(self.sequence)):
            if self.sequence[i] == 'A':
                reverse_sequence[i] = 'U'
            elif self.sequence[i] == 'U':
                reverse_sequence[i] = 'A'
            elif self.sequence[i] == 'G':
                reverse_sequence[i] = 'C'
            elif self.sequence[i] == 'C':
                reverse_sequence[i] = 'G'
            else:
                print('Incorrect type or sequence!')
                self.error += 1
                break
        if self.error == 0:
            self.reverse_complement = ''.join(reverse_sequence)

print('Please, input your sequence:')
seq = input().upper()
print('Please, input type of your sequence (DNA or RNA):')
type_seq = input().upper()

if type_seq == 'DNA':
    x = Dna(seq)
    Dna.gc_content(x)
    print(f'GC-content is {x.gc_content} %')
    Dna.reverse_complement(x)
    print(f'Complement sequence is {x.reverse_complement}')
    Dna.transcribe(x)
    print(f'Transcript is {x.transcribe}')
elif type_seq == 'RNA':
    x = Rna(seq)
    Rna.gc_content(x)
    print(f'GC-content is {x.gc_content} %')
    Rna.reverse_complement(x)
    print(f'Complement sequence is {x.reverse_complement}')
else:
    print('Incorrect type of sequence! Try again')


