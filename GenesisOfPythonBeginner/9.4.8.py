
Количество слов

На вход программе подается строка текста, состоящая из слов, разделенных ровно одним пробелом. Напишите программу, которая подсчитывает количество слов в ней.

Формат входных данных 
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести количество слов.

Примечание 1. Строка текста не содержит пробелов в начале и конце.

Примечание 2. Используйте для решения задачи метод count.

Sample Input 1:

Hello world

Sample Output 1:

2

Sample Input 2:

Python

Sample Output 2:

1

Sample Input 3:

In 2010, someone paid 10k Bitcoin for two pizzas.

Sample Output 3:

9

n = input()

print(n.count(" ") + 1)