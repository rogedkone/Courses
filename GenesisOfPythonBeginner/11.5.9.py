
Количество совпадающих пар

На вход программе подается строка текста, содержащая натуральные числа. Из данной строки формируется список чисел. Напишите программу, которая подсчитывает, сколько в полученном списке пар элементов, равных друг другу. Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.

Формат входных данных
На вход программе подается строка текста, содержащая натуральные числа, отделенные символом пробела.

Формат выходных данных
Программа должна вывести одно число – количество пар элементов, равных друг другу.

Sample Input 1:

1 7 5 7 5

Sample Output 1:

2

Sample Input 2:

3 3 3 3 3

Sample Output 2:

10

Sample Input 3:

8 7 6

Sample Output 3:

0

n, count = input().split(), 0
for i in range(len(n)):
    for j in range(i + 1, len(n)):
        if n[i] == n[j]:
            count += 1
print(count)
