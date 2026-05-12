text = input("Введи любой текст: ")

words = text.split()
chars = len(text)
chars_no_spaces = len(text.replace(" ", ""))

print(f"Слов: {len(words)}")
print(f"Символов с пробелами: {chars}")
print(f"Символов без пробелов: {chars_no_spaces}")