#mrna

protein_to_codon = {
    'F': ['UUU', 'UUC'],
    'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
    'I': ['AUU', 'AUC', 'AUA'],
    'M': ['AUG'],
    'V': ['GUU', 'GUC', 'GUA', 'GUG'],
    'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
    'P': ['CCU', 'CCC', 'CCA', 'CCG'],
    'T': ['ACU', 'ACC', 'ACA', 'ACG'],
    'A': ['GCU', 'GCC', 'GCA', 'GCG'],
    'Y': ['UAU', 'UAC'],
    'H': ['CAU', 'CAC'],
    'Q': ['CAA', 'CAG'],
    'N': ['AAU', 'AAC'],
    'K': ['AAA', 'AAG'],
    'D': ['GAU', 'GAC'],
    'E': ['GAA', 'GAG'],
    'C': ['UGU', 'UGC'],
    'W': ['UGG'],
    'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'G': ['GGU', 'GGC', 'GGA', 'GGG'],
    'STOP': ['UAA', 'UAG', 'UGA']
}

protein='MMGVEIDGKVHYAFMPMQKDMHPNCDIDWASSWSELEYIHYDSNMPSGRQLFKSWEGLCFYFTKKEYCTDEANQRRWTYYIAQFKNTINYILQHTCMCICTTTCDLGWNRRWKWVGEYTDYIMVAMGMDCIQFSEMQLSGKNKPQWAGYDKPFRHREWSYFLVPSNVSFMHPGLHEHSPKTFAHGYEFMSMEDIMGTFKQEDFIWDEYLFSPIITTYKLAKCCNPTPLSWAMPAVVIEFWWIWWPEYTYGEYASTEPFYNIKPGYTFPYHIRPEWVRVNYILIFVYIDNPSMQTVWNAQNITNCHASSIHQCWQNKDFFGRAYDLPCMGWLPNKVWQRNTVMTNNFFYKCFKWQVRVSDYQWIACPGSVTGGEVQNSCMLYQKFDGYEKTSNTHGPNDKMIDRNPIQPDWSKGQYMNQHPGHGFCKPLYNDQSHVEWILDWHSHPTVLFTMRSIRGLHVQIMDWKSITTCHHQMRVVNAFQMDSNRGRIIMWDEKFGWARCMINITLDKCTSMFDDSGQVCHKDRIHAKYDLTIFWVTHVACRYDTYWPEPMEVLQPDPMECMWKQVKCQRCMLNPKYPECKLACGLNHNYGELWYFRKNNNTPLVSHTDEAIKYCHREEDATNPIFYGYSVIRIERKHHFGAGLQERINPQTLTREGFKWCTYLLICDCQDDDIDHQFCAMVQPYGECRCHLRDITLDYHCGNVDQSELRSAIYEPGLQCKCDVGKCTFEEWESHWTQWSWYTYPKLISDSWMWFRNAETAGWHWMTGHHNQQSFQGTTRVMAGDCADLRMTEIRLWVTQCQVRLMKTDAIYCNEIKVLYICGRVSGQSYNVHTMIPESAHCCMYINWYKWRRVCELWVPECEEKHMGGFQDLCWLSKHTKEHKSDKITTCHKKDPCRWDATWPPALSMLKGVWIVPYMNDNFAGAKPSPVCRWQIDPVRVRECCIAGNTYINNPFYPFHFSMEVCWYDYAECDPCAVYHHAFNWSHYITGHVQDAHY'
rna_possibilities=1
for letter in protein:
   symbol_occurrences = len(protein_to_codon[letter]) #count how many times you find it in the dictionary
   rna_possibilities = (rna_possibilities * symbol_occurrences) % 1000000
rna_possibilities = (rna_possibilities * len(protein_to_codon['STOP'])) % 1000000
print(rna_possibilities)
