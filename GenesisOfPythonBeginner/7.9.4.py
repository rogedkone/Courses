
Делители-2

На вход программе подается натуральное число nnn. Напишите программу, выводящую графическое изображение делимости чисел от 111 до nnn включительно. В каждой строке надо напечатать очередное число и столько символов «+», сколько делителей у этого числа.

Формат входных данных
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести графическое изображение чисел от 111 до nnn, каждое на отдельной строке.

Sample Input:

5

Sample Output:

1+
2++
3++
4+++
5++

n, count = int(input()), 0

for i in range(1, n + 1):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    print(i, "+" * count, sep="")
