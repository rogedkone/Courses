
Принадлежность 3

Напишите программу, которая принимает целое число xxx и определяет, принадлежит ли данное число указанным промежуткам.

Формат входных данных
На вход программе подаётся целое число xxx.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Примечание. Если точка выколотая, то граница не включается, если точка закрашенная, то граница включается. 

Sample Input 1:

-332

Sample Output 1:

Не принадлежит

Sample Input 2:

-30

Sample Output 2:

Не принадлежит

Sample Input 3:

-21

Sample Output 3:

Принадлежит

x = int(input())

if x > -30 and x <= -2 or x > 7 and x <= 25:
    print("Принадлежит")
else:
    print("Не принадлежит")
