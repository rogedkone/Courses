
Без дубликатов

На вход программе подается натуральное число nnn, а затем nnn строк. Напишите программу, которая выводит только уникальные строки, в том же порядке, в котором они были введены.

Формат входных данных
На вход программе подаются натуральное число nnn, а затем nnn строк, каждая на отдельной строке.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Считайте, что все строки состоят из строчных символов.

Sample Input:

5
first
second
first
third
second

Sample Output:

first
second
third

n = []
for _ in range(int(input())):
  puk = input()
  if puk in n:
    continue
  else:
    n.append(puk)
print(*n, sep="\n")