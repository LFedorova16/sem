reference = input()
sample = input()
for i, ref_nuc in enumerate(reference):
    samp_nuc = sample[i]
    if ref_nuc != samp_nuc:
        print(f"{i + 1}: {ref_nuc} > {samp_nuc}")
