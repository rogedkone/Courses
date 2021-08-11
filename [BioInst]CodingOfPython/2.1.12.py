

В Институте биоинформатики между информатиками и биологами устраивается соревнование. Победителям соревнования достанется большой и вкусный пирог. В команде биологов a a a человек, а в команде информатиков — b b b человек.

Нужно заранее разрезать пирог таким образом, чтобы можно было раздать кусочки пирога любой команде, выигравшей соревнование, при этом каждому участнику этой команды должно достаться одинаковое число кусочков пирога. И так как не хочется резать пирог на слишком мелкие кусочки, нужно найти минимальное подходящее число.

Напишите программу, которая помогает найти это число.
Программа должна считывать размеры команд (два положительных целых числа a a a и b b b, каждое число вводится на отдельной строке) и выводить наименьшее число d d d, которое делится на оба этих числа без остатка.

Sample Input 1:

1
2

Sample Output 1:

2

Sample Input 2:

7
5

Sample Output 2:

35

Sample Input 3:

15
15

Sample Output 3:

15

a = int(input())
b = int(input())
i = min(a, b)
while True:
    if i%a==0 and i%b==0:
        break
    i += 1
print(i)
