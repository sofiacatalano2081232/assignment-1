#rna
sequence2 = 'ACTGACGTCAAAGGAACACCCACGGATGATGAAATGTTGTTAGTATGGTGGAGGGCTTATAAGCAGTAATTATTTGGAACCGTGTTGAGGAGTAACATTCAAAAGGAGGAGGAGGTAGATCCGTAAGTGCGAAAATCGGGTACAAGGTTAATGCCGTGAGTCCACATAGGAGGGCGACAGAGAGGGGTAGGCCAAAATTGGCCATGTCGTGTGTTTCTACCGCGGGATCGGACCTAACTAAAAATCAGATATTGAACGTTTCGACCGTGCAAACGTTAGGAAGGATGGCATCGCCTATGCTGGGTTCTCATGCCGGTTTGCGAGGATGTGCAAATGCCCGATGACACCTAACGGAACTAGTTTTGGGGAAGGCGCCACTGCAGGACAACCGCCTTTTTCTATTGCAATATTCCTAAAATATCGCCACTCTCAGGATTCGCTGCATCTGGGTGACGACAGTGAGCTGTCTATCATATACCGATGGACAAACAGCTGAGGTTCTATCCTACGAACAAGTAACTGGGTACGAACGGAAATTAAATAATGGCAATGTCCGAACTAAAGCTTTTGAGGGCGCTACATTCCCTTTACCTGCCCTGATACGTTATCAACTGGGGTTCACGGATTACGGCAATGCCGTCGGCTGTTTCTCACTATGGTTAATCGTCGTCTCCTAGATAATCATCTGAGCGTCCCGCGAAGTATAGGAACCCATAGTCCTTGTTGTTGAGTCCTTCATCCCCCACGGGTTTCGACGCTTTCCCAGTTACTCCGATCTAATAGACATTCCAGTGTTATGAACTGCTATGCCAATAAGTGAGATCAAATCAAAAACTTGCTGGGTTCCGGGCGGGTATGAAGACCACCTTGTTTAATAAAGGCAAGTTGGGTAGACGTGCTTTGTTTTCAGAGGTCATAAGTTTTGTAAGTTCACACTTTAGAATGAGTGCGAACAGATAGGC'
new_sequence = '' 
for symbol in sequence2:
     if symbol== 'T':
          new_sequence+= 'U' #exchange T with U
     else:
          new_sequence += symbol

print(new_sequence)
