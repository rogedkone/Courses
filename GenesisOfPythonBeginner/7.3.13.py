
Наибольшие числа 🌶️🌶️

На вход программе подается натуральное число nnn, а затем nnn различных натуральных чисел, каждое на отдельной строке. Напишите программу, которая выводит наибольшее и второе наибольшее число последовательности.

Формат входных данных
На вход программе подаются натуральное число n≥2n \ge 2n≥2, а затем nnn различных натуральных чисел, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести два наибольших числа, каждое на отдельной строке.

Sample Input 1:

5
1
2
3
4
5

Sample Output 1:

5
4

Sample Input 2:

8
9
7
5
4
3
2
78
1

Sample Output 2:

78
9

Sample Input 3:

13
1
2
3
5
8
233
13
21
34
377
55
89
144

Sample Output 3:

377
233

n, largest, prelargest = int(input()), 0, 0

for i in range(n):
    n = int(input())
    if n >= largest:
        prelargest = largest
        largest = n
    elif n >= prelargest:
        prelargest = n
print(largest)
print(prelargest)
