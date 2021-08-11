
Все вместе

Дано натуральное число. Напишите программу, которая вычисляет:

    сумму его цифр;
    количество цифр в нем;
    произведение его цифр;
    среднее арифметическое его цифр;
    его первую цифру;
    сумму его первой и последней цифры.

Формат входных данных 
На вход программе подается одно натуральное число.

Формат выходных данных
Программа должна вывести значения указанных величин в указанном порядке.

Sample Input 1:

5678

Sample Output 1:

26
4
1680
6.5
5
13

Sample Input 2:

132

Sample Output 2:

6
3
6
2.0
1
3

Sample Input 3:

75

Sample Output 3:

12
2
35
6.0
7
12

n = int(input())
value_sum, value_len, value_umn, value_first, value_end = 0, 0, 1, 0, n % 10

while n != 0:  # пока в числе есть цифры
    last_digit = n % 10  # получить последнюю цифру
    value_sum += last_digit
    value_len += 1
    value_umn *= last_digit
    n = n // 10  # удалить последнюю цифру из числа
    value_first = last_digit
    
print(value_sum, value_len, value_umn, value_sum / value_len, value_first, value_first + value_end, sep="\n")
