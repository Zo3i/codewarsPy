def DNA_strand(dna):
    def change(s):
        if s == 'A':
            return 'T'
        elif s == 'T':
            return 'A'
        elif s == 'C':
            return 'G'
        else:
            return 'C'
    return ''.join(map(change, dna))
print(DNA_strand("AAAA"))

#############大佬的最佳实践
def DNA_strand(dna):
    return dna.translate(string.maketrans("ATCG","TAGC"))