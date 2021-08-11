
Корректный ip-адрес

На вход программе подается строка текста, содержащая 4 целых числа разделенных точкой. Напишите программу, которая определяет является ли введенная строка текста корректным ip-адресом.

Формат входных данных
На вход программе подается строка текста, содержащая 4 целых числа разделенных точкой.

Формат выходных данных
Программа должна вывести «ДА», если введеная строка является корректным ip-адресом, и «НЕТ» — в противном случае.

Примечание. ip-адрес является корректным, если все 4 числа находятся в диапазоне от 0 до 255 включительно.

Sample Input 1:

192.168.0.3

Sample Output 1:

ДА

Sample Input 2:

192.168.0.300

Sample Output 2:

НЕТ

n = input().split(".")
answer = "ДА"
for i in range(len(n)):
    if int(n[i]) < 0 or int(n[i]) > 255:
        answer = "НЕТ"
        break
print(answer)