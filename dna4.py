dna = input()
gc_count = dna.count("G") + dna.count("C")
gc_pr = (gc_count / len(dna)) * 100
print(f"{gc_pr:.2f}%")
