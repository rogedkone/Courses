
Only even numbers 🌶️

Напишите программу, которая считывает последовательность из 10 целых чисел и определяет является ли каждое из них четным или нет.

Формат входных данных
На вход программе подаются 10 целых чисел, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести строку «YES», если все числа четные и «NO» в ином случае.

Sample Input 1:

2
4
6
8
10
12
14
16
18
20

Sample Output 1:

YES

Sample Input 2:

1
2
3
4
5
6
7
8
9
10

Sample Output 2:

NO

n, count = 0, 0

for _ in range(10):
    n = int(input())
    if n % 2 == 1:
        count += 1
if count > 0:
    print("NO")
else:
    print("YES")
