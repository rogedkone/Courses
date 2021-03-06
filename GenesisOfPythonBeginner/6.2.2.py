Евклидово расстояние

На плоскости евклидово расстояние между двумя точками (x1; y1)(x_{1}; \, y_{1})(x1​;y1​) и (x2; y2)(x_{2}; \, y_{2})(x2​;y2​) определяется так ρ=(x1−x2)2+(y1−y2)2\rho = \sqrt{(x_1-x_2)^2 + (y_1-y_2)^2}ρ=(x1​−x2​)2+(y1​−y2​)2

​.

Напишите программу определяющую евклидово расстояние между двумя точками, координаты которых заданы.

Формат входных данных
На вход программе подается четыре вещественных числа, каждое на отдельной строке – x1, y1, x2, y2x_{1}, \, y_{1}, \, x_{2}, \, y_{2}x1​,y1​,x2​,y2​​.

Формат выходных данных
Программа должна вывести одно число – евклидово расстояние.

Sample Input 1:

2.0
2.5
44.155
100.50

Sample Output 1:

106.68197610187018

Sample Input 2:

5.5
2.4
4.9
6.3

Sample Output 2:

3.9458839313897713

Sample Input 3:

150.0
100.0
50.0
10.0

Sample Output 3:

134.5362404707371

import math
x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())

print(pow(pow((x1 - x2), 2) + pow((y1 - y2), 2), 0.5))
