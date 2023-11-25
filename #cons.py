#cons

from Bio.Seq import Seq
from Bio import SeqIO


dna10_1 = ''
dna10_2 = ''
dna10_3 = ''
dna10_4 = ''
dna10_5 = ''
dna10_6 = ''
dna10_7 = ''
dna10_8 =''
dna10_9=''
dna10_10=''

fasta_file = 'rosalind_cons.txt'
with open(fasta_file, "r") as file:
    records = list(SeqIO.parse(file, "fasta"))#we use it to list the dna strings
    # Verifica che ci siano abbastanza sequenze nel file per le variabili dichiarate
    if len(records) <10:
        print("fasta file doesn't have enough sequences")
    else:
        dna10_1 = str(records[0].seq)
        dna10_2 = str(records[1].seq)
        dna10_3 = str(records[2].seq) 
        dna10_4 = str(records[3].seq) 
        dna10_5 = str(records[4].seq) 
        dna10_6 = str(records[5].seq) 
        dna10_7 = str(records[6].seq) 
        dna10_8 = str(records[7].seq) 
        dna10_9= str(records[8].seq) 
        dna10_10 = str(records[9].seq) 

sequences = [dna10_1, dna10_2, dna10_3, dna10_4, dna10_5, dna10_6, dna10_7,dna10_8,dna10_9,dna10_10]

length = len(dna10_1)
pos = 0
aRow = [0] * length
cRow = [0] * length
gRow = [0] * length
tRow = [0] * length

while (pos < length):
    for sequence in sequences:
        base = sequence[pos]
        if (base == "A"):
            aRow[pos] = aRow[pos] + 1
        elif (base =="C"):
            cRow[pos] = cRow[pos] + 1
        elif (base =="G"):
            gRow[pos] = gRow[pos] + 1
        elif (base =="T"):
            tRow[pos] = tRow[pos] + 1
        else:
            print("error1")
    pos = pos + 1
#once we have the numbers we have to get the sequence and create the matrix
consensus = Seq("")
aCount = 0
cCount = 0
gCount = 0
tCount = 0
maxCount = 0
pos = 0

while (pos < length):
    aCount = aRow[pos]
    cCount = cRow[pos]
    gCount = gRow[pos]
    tCount = tRow[pos]
    maxCount = max([aCount,cCount,gCount,tCount])
    if (maxCount == aCount):
        consensus = consensus + "A"
    elif (maxCount == cCount):
        consensus = consensus + "C"
    elif (maxCount == gCount):
        consensus = consensus + "G"
    elif (maxCount == tCount):
        consensus = consensus + "T"
    else:
        print("error2")
    
    pos = pos + 1
    
print (consensus)
print(aRow,cRow,gRow,tRow)
#for the matrix
print("A: " + ' '.join(map(str,aRow)))
print("C: " +' '.join(map(str,cRow)))
print("G: " +' '.join(map(str,gRow)))
print("T: " +' '.join(map(str,tRow)))



#another way
# ^_^ coding:utf-8 ^_^

"""
Consensus and Profile
url: http://rosalind.info/problems/cons/

Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)
"""

from Bio import SeqIO
import numpy as np
np.set_printoptions(threshold= np.inf)

# load data
seq_name, seq_string = [], []
with open ("rosalind_cons.txt",'r') as fa:
    for seq_record  in SeqIO.parse(fa,'fasta'):
        seq_name.append(str(seq_record.name))
        seq_string.append(str(seq_record.seq))

seq_len = len(seq_string)
str_len = len(seq_string[0])

symbol = ["A", "C", "G", "T"]
consensus_string = ""
profile_matrix = np.zeros(shape=(4, str_len), dtype=int)

for c in range(str_len):
    position_symbol = [s[c] for s in seq_string]
    most_common_symbol = max(position_symbol, key=position_symbol.count)
    consensus_string += most_common_symbol
    for r in range(len(symbol)):
        profile_matrix[r][c] = position_symbol.count(symbol[r])
    
print(consensus_string)
for i in range(len(symbol)):
    print("{}: {}".format(symbol[i], " ".join([str(j) for j in profile_matrix[i]])))