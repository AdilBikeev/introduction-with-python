# Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных файлах (в одном файлике отрывок из какой-то книги, а втором файлике — сжатая версия этого текста). 

def rle_encode(data):
    encoded = []
    count = 1
    for i in range(len(data)):
        if i == len(data) - 1: # Если последний символ
            encoded.append(str(count))
            encoded.append(data[i])
        elif data[i] == data[i + 1]: # Если символы повторяются
            count += 1
        else: # Если символы не повторяются - сжимаем ААА -> 3A
            encoded.append(str(count))
            encoded.append(data[i])
            count = 1
    return ''.join(encoded)

def rle_decode(data):
    decoded = []
    number = 0
    for i in range(len(data)):
        if data[i].isdigit():
            number = number * 10 + int(data[i])
        else:
            decoded.append(data[i] * number)
            number = 0
    return ''.join(decoded)

def read_text_from_file(file_name):
    file = open(file_name, 'r')
    data = file.read()
    file.close()
    return data

def write_text_in_file(file_name, text):
    file = open(file_name, 'w')
    file.write(text)
    file.close()

input_text = read_text_from_file('input_text_rle.txt')
output_text = rle_encode(input_text)
print("Исходный текст: ", input_text)
print("Кодированный текст: ", output_text)
write_text_in_file('output_text_rle.txt', output_text)
print("Раскодированный текст: ", rle_decode(output_text))