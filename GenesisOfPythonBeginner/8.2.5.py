
Третья цифра

Дано натуральное число n (n>99)n \, (n > 99)n(n>99). Напишите программу, которая определяет его третью (с начала) цифру.

Формат входных данных 
На вход программе подается одно натуральное число, состоящее как минимум из трех цифр.

Формат выходных данных
Программа должна вывести его третью (с начала) цифру.

Sample Input 1:

100000000

Sample Output 1:

0

Sample Input 2:

3459087654

Sample Output 2:

5

Sample Input 3:

134

Sample Output 3:

4

n = int(input())

while n > 999:
    n //= 10
print(n % 10)
