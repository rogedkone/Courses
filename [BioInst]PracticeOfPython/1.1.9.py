

Если приведенная ниже задача кажется вам сложной, то вам следует пройти первый курс по языку Python, который не требует начальных знаний языка: https://stepic.org/course/Программирование-на-Python-67﻿.

Реализуйте программу, которая принимает последовательность чисел и выводит их сумму.

Вашей программе на вход подается последовательность строк.
Первая строка содержит число n (1 ≤ n ≤ 100).
В следующих n строках содержится по одному целому числу.

Выведите одно число – сумму данных n чисел.

Примечание:
﻿Чтобы считать одно число из стандартного потока ввода, можно использовать, например, следующий код

n = int(input())

Sample Input 1:

2
2
3

Sample Output 1:

5

Sample Input 2:

2
-2
-2

Sample Output 2:

-4

Sample Input 3:

1
31

Sample Output 3:

31

print(sum(int(input()) for _ in range(int(input()))))