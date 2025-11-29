purchases = {}
with open('purchase_log.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        if line:
            parts = line.split(' ', 1)  # Разделяем на 2 части
            if len(parts) == 2:
                user_id, category = parts
                purchases[user_id] = category
# Вывод первых двух элементов
print("purchases:")
for i, (user_id, category) in enumerate(purchases.items()):
    print(f"{user_id} '{category}'")
    if i == 1:  # Останавливаемся после второго элемента
        break