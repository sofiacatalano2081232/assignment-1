#dna
sequence = 'AACGCGAGACTTCCTACTCTTCAATGGGAGATGGTTAAACACACTAAATATTGTATACTTCAGCTCAGTCGTTTCCCCAGGCAGAGTCTGCACTTGACAACGCCATCATACAAAATACCTAGTCCGGAGGGGCCTACGGGCGCCCTCACACTGATATAGTAAGTGTTCTTAGGAGTCCTGCTAATCATTCAGCAACGCGAATGACTCTGTAACAGGAAACTTATACCGCAATTAGTCTGTGTCAGTGCCCGAATGCCACGGGGAGCCGGTAGCAGAACACGGGACTCCTGCCGAATCCAAACTAGACAGCTCTATCGGTCCGCGATGAACATACATCAGTACGCGCTGATACTCACCGTTCAACCTGGTAGATATAGAACAGGGAACTCATCCCCCGAAATCCCCCCAAAGCCGATTTTTAGTGCGTTATCCGGGGCAGGCTGTGCAAGGGTGGTTTCATTGCTCCATCTGCAGCGTTCTTTCTCGGAGGGTGATTTCGCTGCGGTGCTTGGGATAGACACAACCTGCCCCATTATTTGTAGTGATAGGCGTAGTTTCCCTAACGATTATGCGTCTGAAGTGCCACCAGAACTACAGGTTCAGCTGATTGTCCACGATCTGGGAGAACATGGGTCTAGATAGAGTTAATTTGTCGGACCCCGAGCCGCTCGAAAGACAGTATAGCTACCGCGATATGTTCACGCTAACTTTTCTAGTGGGTTCTGAAAAGTGACGGACGGTTGCATGGGAGGCGCTGTATTAGTCTACAGTGCGACCAGCGATAGTACCTGTAGCGTACGGTTCAAAAATGTGTTTTACCATGCCGCCTACATCATGTAAACTCGTCGGGCCCACTTATTCTTAACAACCGTAGGACTTCGATTGAGTCTGCTGTCATGATAGCCGCAGAAGGACCTCAAAACACCAGCCGGTCACGAAGTGCCACTGGGTCGGATATTTTCTTACCGACTGTAGCCACTTATATTATAGATATGT'
#initiation of symbol quantities
numberA = 0
numberC = 0
numberG = 0
numberT = 0
#analyze the sequence letter by letter
for symbol in sequence:
    if symbol == 'A':
         numberA= numberA +1
    elif symbol == 'C':
         numberC = numberC +1
    elif symbol == 'G':
         numberG = numberG +1
    else:
         numberT = numberT +1

print(numberA, numberC ,numberG, numberT)


