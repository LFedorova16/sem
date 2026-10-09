dna = input()
reverse = str.maketrans ("ATGC", "TACG")
reverse_compl = dna.translete(reverse)[::-1]
print(reverse_compl)
