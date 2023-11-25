#tran

transitions = 0
transversions = 0
from Bio import SeqIO

# Define the path to the FASTA file
file_path = "rosalind_tran.txt"  

# Open the FASTA file and use SeqIO to parse it
sequences = list(SeqIO.parse(file_path, "fasta"))

# Check if there are exactly two sequences in the file
if len(sequences) == 2:
    # Access the first and second sequences
    sequence1 = sequences[0]
    sequence2 = sequences[1]
    # Access sequences
    sequence_data1 = str(sequence1.seq)
    sequence_data2 = str(sequence2.seq)
    seq1=sequence_data1
    seq2=sequence_data2    
else:
    print("The FASTA file does not contain exactly two sequences.")
#now that we accessed fasta file, code for the ratio between the sequences

if len(seq1) != len(seq2):
    raise ValueError("Sequences must be of the same length for comparison.")

nucleotide_properties = {
    'A': 'purine',
    'G': 'purine',
    'C': 'pyrimidine',
    'T': 'pyrimidine',
    'U': 'pyrimidine'
}

for symbol1, symbol2 in zip(seq1, seq2):
    if nucleotide_properties[symbol1] == nucleotide_properties[symbol2]:
        if symbol1 != symbol2:
            transitions += 1
    else:
        transversions += 1


ratio = transitions/transversions
print(ratio)
