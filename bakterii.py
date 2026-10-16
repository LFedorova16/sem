growth = []
for _ in range(3):
    line = input()
    culture = [int(x) for x in line.split()]
    growth.append(culture)
threshold = 5
for culture in growth:
    found_index = None
    for i, value in enumerate(culture):
        if value >= threshold:
            found_index = i
            break
    if found_index is not None:
        print(found_index)
    else:
        print("Отсутствует")
