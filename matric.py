sequences = [
    "AACG",
    "AATG",
    "TATG",
    "TTTG"
]
n = len(sequences)
for i in range(n):
    row = []
    for j in range(n):
        if i == j:
            row.append(0)
        else:
            distance = 0
            for pos in range(len(sequences[i])):
                if sequences[i][pos] != sequences[j][pos]:
                    distance += 1
            row.append(distance)
    print(*row)
