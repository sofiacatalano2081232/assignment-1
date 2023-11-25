#prot
# Define a dictionary that maps RNA codons to amino acids
codon_table = {
    'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
    'UAU': 'Y', 'UAC': 'Y', 'UAA': 'Stop', 'UAG': 'Stop',
    'UGU': 'C', 'UGC': 'C', 'UGA': 'Stop', 'UGG': 'W',
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
}

rna_sequence = 'AUGCGCCAAAACAUAGCAGCUCUUGGACAGAAGAUCACAGGGGGCUGGCCCCUUACAAACUAUGUACUACUCGGCAUUUUUCACCAACCAUGUAUUUGCGGUUUGCCAACCCCCCGCUCACCACCGAAUUCGUCCCUGUUAAUAAGGGCGAGCAUGCUAAGGAGCGUCGAGGUAGAAGUGCUUUUGAAAAGACGCACAGGUUGCAUGAUUCGUCAGAACUACGAGUUAUGUGUGCUGACCCCUACUCGGGCGAGCACUACGCGCAUCUUUGGAGCCUAUUACAAGCUUUCUUAUGGGGGCGCCCCAAUCUCCCACGCGCCGUCUCCAUUAAGAUGGGGGGUGCGUAAUUCAGUCACCGGCUGUACGAUCAGAGGCCGGAUGCACCGGAACCUUACCAGUGGACGUUUGGCGGCCAAUGCGGGAUGUGAGCCUUUCCGUCCCUCAAUUCGAUCUAAGCCCAAUUAUGCCUUAAUCAGUAGGGCCUGGGGGCGUCUCAGAACUGUUCGUGUACUCUACCUGGGAUUCGAGUCGUCGGAGCGUCACCAGUGUGGUGGUUCUAGCCGAACCACUCACAGGACGCUCACAUAUGGUGCUGGACAACGAGGCAGCAUGACUCUUCUAAUCAAUCUAGUUCAGGUAUUUAAUCAAUCCACGAACCGAGUCCAACUCAAGAUCGUUCUCCGGACUGAACAGUACAUGACACUCCGGGAACUGUUUAUCGCACAUCUGGCAUGGCUAUUGCACGAGGUAGGGUGGGGGAAGUUUGAAUGCUGUAGUGGUAAGGCGUGCGCACGUAAUACGGCGGUACCGCUCCAAGAAUCAUAUAGUCUAAGUUCUAUUAUACACGUCUUUCGACGUACGUGUUUAACACGCUGUCGGUAUCCAUUCACUCCGGCCCUUACGGGUAAGAUACUGCAAUCGUGCCGUGUGCGGUUCGAUCCAAUGGCACAGGGGCUGCGCAUAGGGCGCCCAGGGCUAAGAUACCGGAUUGUAAGUUACUAUCCUGCGCCCCUAUGGAUACCGCCCAUCAGGCAUUCCACGAGCCACGGAAUCACCAACAGAUAUAGUGUUACCUCUAAUUGCGUUUUAAUCUCGCGCGAACAGCAUCAGCUUAACAUACCUGCUUGGAGGCGUGAGUCAGCCAACCAACCUGCGUUUUUCUCGUCGAGUGGUCAACCAGUGAUCUCUCAGCCGCGGUUGCAAUGUAGUCUAAAGCACGCAGGUAUAGACAUCGGUGUAUUAGUCACCGUAUUACACUUGCGGUUGCCUCGGUUAUUUCGUGUAGUUGGGGAUCUUCGAUAUGCGCGGAUAGGCUACCUUCCUCCAUUAAGUGGAAUGCACUUAUCCCCGAUCAUUUCAGGGUUGCAACCUUUCUUGAUAGCAUAUUCUUUCUUCAGUAAGUCUAUACUCGCCACUGCGGCGGUAAUACGUCAUUCUAUCGAAGCGGGAGCCAUGGAAGCUAUGACUUCCGGUUAUGACAAUCCCAGGAAGCGUACACUUGUCUCGCAUUCAACGACCUUAACCUUCGACGAGGCAUCACGAGCGCUUAACGAUUACCCGCCUGUACGAACACGGGGUUCUAGAUCUCUAUUGAAUGGGAUCGUGACUCAAUAUUGUCGAAGCUCGCAGCGCCUAGCGAUGGGUCAUCAUCGGUGCAGUCUGGCUACAGUAAAACGGGUGCGAUCCGUGUCGGCUCGUGGCGUCCGCCUUGUUGUAUAUUUUCUACUCGCGCGCGGGCUUGUUUUGGACCUACAGGUCAUUGGUCCGCACGGGGUUAACGUAAAGUGCCAAGUAGCGCUAGAGCUCAGCCGAGGGGUCGGUAACGCAUACUCCUACGUAGGGUCUUUUCCCUACAGGGUGUCUCUAGACUAUUCGGAAAUGCAAUGGGGAAACAUCUUAGCCAAACAUGUCCCGCGUGAUAUCGGGACAAAUCCGCGGCCGACCGGGUUUUACAGAUGGCCGAGUGUAAAUUUCGUCACGGAUAAUCUUUAUCCAUACCUCAACUUAAUAUGUUCGACGAACUAUGAGAGGGAUGAGCUUAUCAACGUUGUUUGGGUAGAUAUAUGUCCCGUUUUUUCACGGCUAGAUAACACACACAAGCCGGGCUCACAUUCAAGCGACUGUACCAGCGGGUGUAGAGGGCCAGCAUUUGAGGGGGGAGUCCCGGAACCUCAAACACCUAAAAAUCGAACUGCCCCGCGUCCAUUCGCGGCUCUUUACUUCGGCAUCGUCAUGAGCGAGAUAGUGGUGGACAGGGUUCUUCCUCCCAAUUGGAGACCGCCUUGCCUCAGGCUUACUGUGCAGUGGGGAAAGUUCUGGAGGGGUCUUCGAGCCUCAUGGCAGUUGUACAAAAGAAGUAUUAAUUUGCUGGACCGGAUCGGACAAUUCCCAUCAAGGGGCAUAGUAGAUAACGGGCGAGGUAGAAAAGGCUCGCCUUACGAUGCGGAAUGGUGCGUCGGGGCCAAUACGCUACAUUCGCCUACCCUGAUGGGUGGGUUGCCCUUAAUCAUUCUGGGGUCGCACCGCUCGCAACAUUCUUUACCGAGUUUAGUCGGACCACCGCAACCACGUAAGGCCUUCGGUGCGGAGAUAGGAUCUAAGACAUACGGAGGACUCAGGUUGGAAUGGUCCCGACUGGGUGACUCGAGUGCUCCCGGAACCCGACAUACAGCGAGUCUGGCCAGCUGCAGAUAUGGAAUAGCGGCUAACGGAAGAGGUGCGCUAAUAAAAUCACCCAGACUACAUGUGUCUUCGCCCGCCGAUUGGACGAUUUCUACUCAGAAAAGUUGCGAAAGUAGUUACAGCAACCCCACCCGAGGGCAUAAGAGAGAUAAGGCGGACUGCGUCGAAAGACCUAGCCAGUCCCCUUGCUUUAAUCAGCACCCUCAGUCCUGUUACCCUGGGCGCAUCGGCGCCAUUAGCAGUUCUACUAGGUUGCACCGACCUUCCCCGAAUCGAUUUAUAAACUUAGUGUGUGAUACUGGUGUUAGCCCUAAGGGCCAACUCAGUCCAAUAUUAAUUCCCUUAGACGGUCUUGAUCGUGAACAGGGAGGCUUGGACCUCAAACGAAGUCCCUUGUAUAUAGAUGGACUCUCACUGGCGCCAUAUGACAACUGUCUCGGAAUCCCUCGUAUUCCUCUCGGAGUUGCAAAGGGGUAUGAGGUAGUACCUAAUUGCGACACACCUAUUUCUAUUGUAAUUCUCAUGCCGGCGCGCUCAAUGUGCCCACGUCGAGAACCACGGCUCGCCUCCUCCAAAAUUCAUCGGCGCGAAAUCUGCGUUGGUUUAGAAAAGACCAACCUAGAGCUGGCCGGUUCUGACAGGGGCAGGCUGACACUCCAGCCUGCCGUACAACGCUACAGGAGCCGAAUGGUAAAAAUUCUGAAGUGCCUGACAUUGCUACCCAUGGCGGAUAGGAGCGACCCUCUAGACUCCCCCACGCUAAGGCAACCUAUACCUGCGAAAUCAGGAGCAGUUACACCGUUGGUGCGCUUCAAAAAAGUAGCGUCAAUUGCACGGGUUGCACUAGAGUGUACUCCGGAUUGGCGGCAACGCAGUAGUACAAGUAAAACUGCGCUCGAGAGCCGCUUUGGAAGAUAUCUUCACUCUGCCAUUUGUAAUCAUGUGGCACGGUUGAGCGCUGGCCAGGCUACAUGUAUUGACUUGGAUCUCUUAUUAUACAGUCCAAGCUGCUGCACCAGUCGAACCUAUUUAAGGUACAAUUCCUUUUUGAUAGACCGCCAUCCUUCAUUCUCGGAGAUAGCUCGUGGAUAUUUAGGCGUCAGAGGGGUAAAUAAGGUGUAUUUUAAAACCUUGCGCUGUUAUCGUGUUUGGUGUAGAAGAGAUAGUCCCCUGGUGUUUAUUCGAUUCUUCAGAGUUUAUGAAGAUACACCCAUAUUCGAAUGCUCAACCCGGUCACACUCCACUAUGGCAACCUUCGUUUUCGAGAGAAUUGGGCUUCGACACAUGAUUGAUGCCAGUUACUAUGUCACGAAUAGCCCCAGGCGGGACGUUGCCUAUCGUCUGAGUGUAGUUUGGCGAUCCCGCUGCUGUGAUAGCUGUAUCAAAUUGGAGUUUAUGCUCAUUCUAUGGCUCAAACGCGUGGGGCCACGCCUCAGGUCUAGGUUCGUGUUCUAUGGAGAUCAGCACUCCUCUUCACCUAAUAUACGACGAGUAGUAAAUUCCGGUCCUAAUGUGGUACACUCACGAUGUACUCACGUGUAUACGCACCGGCCGAAGAGGCCGUCGUUCACACCCCACCGCGCUCAUUGUCCUAUUCUUGUCGUACAGCUACAGGACCGCGCCGAAGUACGGGGUCAAUCAAGCGUUGGCCGUGUGCGUAUAUUAAGCCAGUGGCGUGCCCAAAAGCAAUUCUAUUUUGAGGCGUUUGCACGGCCUUCUCGCGGCCUGAACUCCUAUCUGGAAAGCCGCGCUCAGCUCGGUCUUUCCUUAGCGUUGUCUCGAGGCAUUAGGAAGAAGGUACUAGGAGACACAAAUAUUCGAACAUAUGAAGGUCCCGUUAUAGUGAUGGAAACCGAUGGCAUGUCUAAGUCAUUCAUAAUUACCACGGAAUAUCCUGAGGUGCCGCCCACUUAUGUGCGGGUUCGUGUCGGAAGUCCGACUUGCACACACUCAGGCCAUCCAGAUGGAAUUUACUACCGAACCGCAGGACUAGCUGAGAGACUAAGAUUACAGGGUGAGAGUCGCCAAAAGAUGAUGCCAAGCGUAUGCAAACGGCGACGGCUUUAUGUUAUGUCACACCAUUUUGUCGGGGCGGACUGGUUUCGGACACCUGUGCGACUAGCAGUAGUCUCCUACCAGAGCCCUCUCAACGCGGCUUUGGAGAAUCAACCGUCUGCGCUCGCCUGCUUCCCUGAUCCUUAUCCCUUACUAUUGGUCAUAUCAUUAGCGCUGGCACACACAUUCUUGUGCGGUGGGAGUUUUCAAGACUCGAGCGCUGAGCAUCCCUCUCAGCCGCAGGUGUUCAACAGGAUUCUGACUAAGCUACAACAACGAUCGUGUCCUGGUCGAAACGAGGUCACUCUUAAUUUGUAUACAAGAGGAGGAAGAGUCUCAAACCUGGCCUCUAGAGGCUGGUUUCGCCUCGUAAACUACAGUGCGAAACCCUUCAUUCAGGAGCGGGCUGGAUGGGUCCAAUACGAGCCGAUAACUGCUAAAGUUGUUGUUAAAAGAUUUCAGUUGGGGGAGCAGGAUACACAUGUUUUAGAUAACAUUGAUACGUAUUCAAUGCUUUCGAUCUACGGGGGUCAACCACCAGAGCCUGUGCAACGUACCUCGGGAAACGCCCUAUCGCCGAUUGAUACAGUUAGUAGUGUAGGCCAACACAAUCCGGUCAGCCACACCCGCCGCCUCCUAUUGCCCGCCCCCCAGGUCAAUCAUCUCGUGAGCUGGGUCCUAGCUUGUUGGAUUAUCCGGAGUAGGGGCGAAGGGGGUCUCUUUGGCGACGGUCUGAUUUGCAAACUGCGUAGAUCACAAAACCGGACGGAGGUUCUUGGGCAUGACUGUGCGACACCGCACACGAAGGUGUUUCACAUACUUAGCGCCUUAGGAACCAGAGAGUCUGACUCGCUCCGACCUCUAAACCCCCCACAGUUUAUUACGGAGAUUAACAUCCGGACUACCCGAAUGAAGACUAUUAAUUUCCUAAUAUUCGGGUCGGACUACCGUUGGGUCGUACAUCCUAACUCAGCCCGGCCGCUCCGUCUGUGCCCCAAAGUACACCCCUCGGAUAAGACGCCCCCGAUCAGCUGCGUAGGGUCCCUCCACCCAUUGCCCGCAGUCAGCCUCGACUGGACUAGAUGGGUAACGGUUACGGAGCAGGCUGAGCCCUGGACCAGUAAGUGGCCCACAUCGGAGCAAGGACGAGUCCCUUGGGCUCUCAAAAAGAUGAUGCGUUCGCCCCUGUAUAUUGGAAGUAAAGCGUACUGCCGUUGUUUCGCACUAAUAGUGUCGGGGAUCUUAGGCAGUGAGCCGUCCUAUGAACGCGUUGCUCAACGGACACAGCUUUAUUUGCGAGGAUGGAGCAAAGAGUCGUCGACCAUGAUAGUUAAGAUAGGUAUUGAAUACGCCCUGGCCGGCACUUCUGUUCAGAAAGGCGAGACCAACGUUCUAGUGUGUCCGCAAUCGAUCGGCAGGUAUCCAAGAGAGGCUUCGGUCUGCGGGGGCAAUUGGCGUGGCCGGCGCAGCUGCCGGGCAGCCGGGGAACUUACUUUCGCCGUUGAGCACCGCAAUUGCGGUGUUCUAACAUGUUUCUUUCCAGGCGUCCCUCGAAACGACAGCGCUUGCUUACUUUCAUAUCCGCAGUGUGCGAAUCCCAAUAUCGUAUGUCCUCAUCUGAUAGGGACUAGCUUACUACGCGUUCAGAUUUCCCUGUACGAGCAAGUUGUUGACGCGGUCUGUAGGGACUCACCCAAUUGGGGACACCUUUUAGCCAAUUUGACCCUUUGGGGUUUGAUCUGGAGAGAUCUUCAGAACGACGUUCAGGACUUGAUCGAUAAAGUCUUCGCACGCUUUGAGGCUGAGAACAUUUCGAUGAAGCCUAAGUACUUACACGUUCGAGCAUUUGUAGACUGUCUGGUCUGUAUAACCGAAUGUGGCGUUCAGGUCCACAUGGUAUAUCCAUGCCAACGUCCUUGGCCAAGUGUCUUCACGAUAUGUUGGCUUGAGCCGUCUACGAAGGCAUGUCAAGCUGCACUAUUGAGGAGAGGAGGACUUACGGUAGCAGGGGAGAACGGCUAUGCCAACACUCAUCACAGGAUUAGAAAUGACUGGGUAAGAGUGCAUAGUUCAUCUGAAUGCGUGCAUAGCGGGGAAGGCGUAAGCUCGGAUAGACGAUUUGUAUGCCCGGCCCUGCAUGUGAUUCUUAACUCUGUCGGGCCACACCCUCCGUCGCUCCUGAGAGUCUCGGAAACUCAACGCGAACCCGUUACCGCCAGAGUCGAUCAGGCCCCGUGCUGGUGCGAUAUCAAGCUCAAAGUUGAACGGACUAUAGCGAGCCGGCCGCAUACAGGCCCGCGGACCAGAAUGUACGAUCAUCACAUAAUUCCUCUGUCGACUUGCACACAGCGUAGGACGUUCCCCACAGUCAGGCUGCGCAAGAGUGUCAGAACACGUUGCAAUGUAGAAAAGUUCCGUGUUACGGCGAAAAGCAAGGUAUCUCGGCUGUGGCACCAGAUCCACGUAGUAAGUACGGCAAAAGUCGCCUACUUCGUAGCCUCCGGGUCUAGUUUGAGGCAUCCGUUUCACGAGUUCUGGAGACUGAACGUGGUCCACUCUAUAUCCGAUGGGCAGUGGUAUUCUGUAGAACAUGCCCCCUCUGGCUCUACGGUUGACCGAGGUACAGCGAAAUAUUCGGAAAAGGGCAAGGAAAGUCACGGGGGUGUCGCAACCUUUGCAAAGGUUACCCAAACGGCCUGUUCCGCCUUUGGGCCCGUAAGGGCAACCGUUUGUCGACUGACGCGAGCAAGUUAUUCAUUGAGUAGGUCUUCGUGGUCACGCAGGGCAGUGCCAAGCUAUGGGGUAUGCACAUUGGCGGAGAAGAUACUGAGUAAUUGCAAAUUCCUAAGGGUCGGCGGGUCUCAUAUGGCCGGCAAAUGUUACGGAGUUGUCAUUAUAAGAUUCUUUAGGCUGGGCUGGGAACAAGGCGAGAGAAGUGAAACUCGCCUAUUCGACGCGACGUUAUCAGCAUUACGCGCAUAUGUCAGCCAGACCUGUCAAACUUUAGGGUCUGCUUGGGUUAGCGAAGUAUGCUUUUAUCCUCAAGCCCAGUUAGUAAGACUAGAUCAGCUUCCUGAAAACCUCUCAUUCGCAAAGCAUACAACCGUUAUUACGCUGGCCCCCGAUCACAGUCAUCUCUUUCUGCUUACCCUGGACGACAGCCGGUCAAUUGUCAAGUACAACCGUCUGAAUUUGCGUUUGCAUGGUUCUCGCGAUAGGAUGGGCUGGCAUUGGUAUCGCGAGUACAGUUUUUUUGUAGUCGAAGGGCCAACUUCUGCCUCUAGCGCUUAUGUCAGUGAAAGACUGUUGUACAACCGAAUUACCACUCGCCCAAAACUCUACACUUCAUCCUUAUUCGAGUUAAUCUCUUUGCAGAGCUGGAAUGAUUUAACAGGCACAAGACCACGCGCAGUCGGUUUGAUCUGCCAUGGGAGGCUUGAAUCCCGAUGCCGCCGACCGGGGAACACUGAUGAGGGAUUAGGAGCCGUUAGACGCAAUGUCCUUCAUGCGUUAACGAAGCCCCGGCAUCGCGGUUUACCGACACUGUUUAGUGUGUCCGGGAGUCCUAUACUGAUGGAAGGUUCCCCGCUACGAUUAAUCCAUAUGACGGCCCGCACGGCCAAAAGCCGUGACUUGCUCAUGGAAUCUUGGCGGGUUUCCAGUGCAGGACCGAAUAUUUGCUUGCCGGGCCACGGUGCGCUGCAGACAGCAAGUCGGCUCGCGGUGCAAGGCGAUCGACUUUCAUUUAGUGGCCUCGAGGUACCCCGGCCACAGUUAGAUUCGCCGUAG'
protein = ''
for i in range(0, len(rna_sequence), 3):
    codon = rna_sequence[i:i+3] # from i position to i+3, we get the codon
    amino_acid = codon_table.get(codon, None)
    if amino_acid == 'Stop':
        break  # Stop codon indicates the end of translation
    if amino_acid:
        protein += amino_acid
    else:
        protein += 'X'  # Replace with 'X' if codon is unknown

print(protein)
