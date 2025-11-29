def debug_solution():
    purchases = {}
    print("СОДЕРЖИМОЕ purchase_log.txt:")
    print("-" * 50)
    try:
        with open('purchase_log.txt', 'r', encoding='utf-8') as f:
            for i, line in enumerate(f):
                line = line.strip()
                if line:
                    parts = line.split(' ', 1)
                    if len(parts) == 2:
                        user_id, category = parts
                        purchases[user_id] = category
                        if i < 5:
                            print(f"  {user_id} -> {category}")
        print(f"Всего загружено: {len(purchases)} покупок")
    except Exception as e:
        print(f"Ошибка: {e}")
        try:
            with open('purchase_log.txt', 'r', encoding='cp1251') as f:
                for i, line in enumerate(f):
                    line = line.strip()
                    if line:
                        parts = line.split(' ', 1)
                        if len(parts) == 2:
                            user_id, category = parts
                            purchases[user_id] = category
                            if i < 5:
                                print(f"  {user_id} -> {category}")
            print(f"Всего загружено: {len(purchases)} покупок (cp1251)")
        except Exception as e2:
            print(f"Ошибка в cp1251: {e2}")
    print("\n" + "=" * 50)
    print("ПРОВЕРКА visit_log.csv:")
    print("-" * 50)
    matches_found = 0
    results = []
    try:
        with open('visit_log.csv', 'r', encoding='utf-8') as visit, \
                open('funnel.csv', 'w', encoding='utf-8') as funnel:
            funnel.write('user_id,source,category\n')
            for line_num, line in enumerate(visit):
                line = line.strip()
                if not line:
                    continue
                if line_num == 0:
                    print(f"Заголовок: {line}")
                    continue
                parts = line.split(',')
                if len(parts) >= 2:
                    user_id = parts[0].strip()
                    source = parts[1].strip()
                    if user_id in purchases:
                        matches_found += 1
                        category = purchases[user_id]
                        output = f"{user_id},{source},{category}"
                        funnel.write(output + '\n')
                        results.append(output)
                        if matches_found <= 3:
                            print(f"СОВПАДЕНИЕ {matches_found}: {user_id} -> {category}")
                    else:
                        if line_num <= 5:
                            print(f"НЕТ совпадения: {user_id}")
                if line_num >= 10:
                    print("... (показаны первые 10 строк)")
                    break
        print(f"\nИТОГ: Найдено совпадений: {matches_found}")
        if results:
            print("\nПервые три строки файла funnel.csv:")
            print("user_id,source,category")
            for line in results[:3]:
                print(line)
        else:
            print("\nВНИМАНИЕ: Совпадений не найдено!")
            print("Возможные причины:")
            print("1. user_id в файлах не совпадают")
            print("2. Разные кодировки файлов")
            print("3. Файлы содержат разные данные")
    except Exception as e:
        print(f"Ошибка при обработке visit_log.csv: {e}")
debug_solution()