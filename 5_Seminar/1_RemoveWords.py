# Напишите программу, удаляющую из текста все слова содержащие "абв", которое регистронезависимо. Используйте знания с последней лекции. Выполните ее в виде функции. 
# Пример: «абвгдеж рабав копыто фабв Абкн абрыволк аБволк»

def where(expression, col):
    return [x for x in col if expression(x)]

def filter_text_by_word(text, word):
    words = text.split()
    filtered_words = where(lambda w: w.find(word) == -1, words) 
    return ' '.join(w for w in filtered_words)

text = input("Введите исходный текст: ")
word_filter = input("Введите слово для фильтрации: ")
filtered_text = filter_text_by_word(text, word_filter)
print("Текст с отфильтрованными словами: ", filtered_text)

    