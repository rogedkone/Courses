
Наименьшее из двух чисел

Напишите программу, которая определяет наименьшее из двух чисел.

Формат входных данных
На вход программе подаётся два различных целых числа.

Формат выходных данных
Программа должна вывести наименьшее из двух чисел.

Sample Input 1:

8
11

Sample Output 1:

8

Sample Input 2:

20
5

Sample Output 2:

5

a, b = int(input()), int(input())

if a < b:
    print(a)
else:
    print(b)
