

Напишите программу, которая выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ... (число повторяется столько раз, чему равно). На вход программе передаётся неотрицательное целое число n — столько элементов последовательности должна отобразить программа. На выходе ожидается последовательность чисел, записанных через пробел в одну строку.

Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.

Sample Input:

7

Sample Output:

1 2 2 3 3 3 4

n = int(input())

count = 0
number = 1
output = []
number_count = 0

while count < n:
    for i in range(0, number):
        output.append(number)
        number_count += 1
        count += 1
        if count == n:
            break
    number += 1

str_output = " ".join([str(item) for item in output])
print(str_output)
