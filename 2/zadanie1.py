def sum_distance(from_, to):
    if from_ > to:
        from_, to = to, from_

    total_sum = 0
    for number in range(from_, to + 1):
        total_sum += number

    return total_sum

print("Реализация функции sum_distance:")
print("-" * 40)

print(f"sum_distance(1, 5) = {sum_distance(1, 5)}") #подсчет простых значений
print(f"sum_distance(1, 1000) = {sum_distance(1, 1000)}") #подсчет значений побольше
print(f"sum_distance(-3, -1) = {sum_distance(-3, -1)}") #подсчет значений отрицательных