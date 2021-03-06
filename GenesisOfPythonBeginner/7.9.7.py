
Простые числа

На вход программе подается два натуральных числа aaa и bbb (a< ba < ba< b). Напишите программу, которая находит все простые числа от aaa до bbb включительно.

Формат входных данных
На вход программе подаются два числа, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести все простые числа от aaa до bbb включительно, каждое на отдельной строке.

Примечание. Число 111 простым не является.

Sample Input 1:

2
15

Sample Output 1:

2
3
5
7
11
13

Sample Input 2:

1
5

Sample Output 2:

2
3
5

a, b, count = int(input()), int(input()), 0

for i in range(a, b + 1):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    if count == 2:
        print(i)
