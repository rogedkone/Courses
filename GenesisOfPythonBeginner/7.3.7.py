
Асимптотическое приближение

На вход программе подается натуральное число nnn. Напишите программу, которая вычисляет значение выражения
(1+12 +13+…+1n)−ln⁡(n).\left(1+\dfrac12 + \dfrac13 + \ldots + \dfrac{1}{n} \right) - \ln (n).
(1+21​ +31​+…+n1​)−ln(n).

Примечание. Для вычисления натурального логарифма воспользуйтесь функцией log(n), которая находится в модуле math.

Sample Input 1:

10

Sample Output 1:

0.6263831609742079

Sample Input 2:

1

Sample Output 2:

1.0

Sample Input 3:

100

Sample Output 3:

0.5822073316515288

import math

count, n = 0, int(input())

for i in range(1, n + 1):
    count += 1 / i
print(count - math.log(n))
