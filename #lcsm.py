#lcsm

def find_longest_common_substring(dna_strings):
    # Take the first DNA string as the reference string
    reference = dna_strings[0]
    longest_common_substring = ""
    # Iterate through all possible substrings of the reference string
    for i in range(0,len(reference)):
        for j in range(i + len(longest_common_substring) + 1, len(reference) + 1):
            substring = reference[i:j]
            is_common_substring = all(substring in dna_string for dna_string in dna_strings[1:])
            if is_common_substring and len(substring) > len(longest_common_substring):
                longest_common_substring = substring
    return longest_common_substring
# Read the collection of DNA strings from a file or input
dna_strings = []
with open("rosalind_lcsm.txt", "r") as file:
    dna_string = ""
    for line in file:
        if line.startswith(">"):
            if dna_string:
                dna_strings.append(dna_string)
            dna_string = ""
        else:
            dna_string += line.strip()
    if dna_string:
        dna_strings.append(dna_string)
# Find and print the longest common substring
result = find_longest_common_substring(dna_strings)
print("Longest Common Substring:", result)