
Среднее число

Даны три различных целых числа. Напишите программу, которая находит среднее по величине число.

Формат входных данных
На вход программе подаётся три различных целых числа, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести среднее число.

Примечание. Средним называется число, которое будет вторым, если три числа отсортировать в порядке возрастания.

Sample Input 1:

1
2
3

Sample Output 1:

2

Sample Input 2:

10
30
20

Sample Output 2:

20

Sample Input 3:

67
100
54

Sample Output 3:

67

Sample Input 4:

54
34
33

Sample Output 4:

34

a, b, c = int(input()), int(input()), int(input())

if a < b < c:
    print(b)
elif c < b < a:
    print(b)
elif a < c < b:
    print(c)
elif b < c < a:
    print(c)
elif b < a < c:
    print(a)
elif c < a < b:
    print(a)
