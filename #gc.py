#gc

from Bio import SeqIO

def calculate_gc_content(sequence):
    # Count the number of Gs and Cs in the sequence
    gc_count = sequence.count('G') + sequence.count('C')
    # Calculate the GC content as a percentage of the total sequence length
    total_length = len(sequence)
    gc_content = (gc_count / total_length) * 100
    
    return gc_content

def find_highest_gc_content(fasta_file):
    highest_gc_id = ""
    highest_gc = 0.0
    with open(fasta_file, "r") as file:
        for record in SeqIO.parse(file, "fasta"):
            sequence = str(record.seq)
            gc_content = calculate_gc_content(sequence)
            if gc_content > highest_gc:
                highest_gc = gc_content
                highest_gc_id = record.id

    return highest_gc_id, highest_gc

fasta_file = "rosalind_gc.txt"  
highest_gc_id, highest_gc = find_highest_gc_content(fasta_file)
print(highest_gc_id, highest_gc)