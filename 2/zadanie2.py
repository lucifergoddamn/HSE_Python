def trim_and_repeat(text, offset=0, repetitions=1):
    return text[offset:] * repetitions
print("Проверка:")
print(trim_and_repeat('chiko'))
print(trim_and_repeat('chiko', 2))
print(trim_and_repeat('chiko', 3, 4))