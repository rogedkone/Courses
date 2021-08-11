
Пол и потолок

Напишите программу, вычисляющую значение ⌈x⌉ +⌊x⌋\lceil x\rceil + \lfloor x\rfloor⌈x⌉ +⌊x⌋ по заданному вещественному числу xxx.

Формат входных данных
На вход программе подается одно вещественное число xxx.

Формат выходных данных
Программа должна вывести одно число – значение указанного выражения.

Примечание. ⌈x⌉\lceil x\rceil⌈x⌉ – потолок числа, ⌊x⌋\lfloor x\rfloor⌊x⌋ – пол числа.

Sample Input 1:

5.5

Sample Output 1:

11

Sample Input 2:

5.4

Sample Output 2:

11

Sample Input 3:

-12.2

Sample Output 3:

-25

import math

x = float(input())
print(math.ceil(x) + math.floor(x))
