rna = input()
coding_count = 0
stop_codon = " "
for i in range(0, len(rna), 3):
    codon = rna[i:i+3]
    if codon in ["UAA", "UAG", "UGA"]:
        stop_codon = codon
        break
    coding_count += 1
print(f"Количество кодирующих кодонов: {coding_count}")
print(f"Стоп-кодон: {stop_codon}")
