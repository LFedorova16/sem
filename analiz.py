nucleotids = ["A", "T", "G", "C"]
accepted_sequences = []
while True:
    user_input = input()
    if user_input == "STOP":
        break
    is_valid = True
    for char in user_input:
        if char not in nucleotids:
            is_valid = False
            break
    if is_valid and len(user_input) > 0:
        accepted_sequences.append(user_input)
    else:
        print("Предупреждение, некорректная последовательность ДНК")
count = len(accepted_sequences)
print(f"Количество принятых последовательностей: {count}")
lengths = []
for seq in accepted_sequences:
    lengths.append(len(seq))
print(f"Длины последовательностей: {lengths}")
