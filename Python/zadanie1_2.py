word = 'test'
length = len(word)
middle_index = length // 2

if length % 2 == 1:
    result = word[middle_index]
else:
    result = word[middle_index - 1:middle_index + 1]
print(f"word = '{word}'")
print(f"Результат: {result}")