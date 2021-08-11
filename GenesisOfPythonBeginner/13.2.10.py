
Сумма цифр

Напишите функцию print_digit_sum(), которая принимает одно целое число num и выводит на печать сумму его цифр.

Sample Input 1:

12345

Sample Output 1:

15

Sample Input 2:

12

Sample Output 2:

3

Sample Input 3:

7

Sample Output 3:

7

def print_digit_sum(num):
    sum = 0
    while num != 0:
        sum += num % 10
        num = num // 10
    print(sum)
# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)
