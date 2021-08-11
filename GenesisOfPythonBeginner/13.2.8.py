
Звездный треугольник

Напишите функцию draw_triangle(fill, base), которая принимает два параметра:

    fill – символ заполнитель;
    base – величина основания равнобедренного треугольника;

а затем выводит его.

Примечание. Гарантируется, что основание треугольника – нечетное число.

Sample Input 1:

*
9

Sample Output 1:

*
**
***
****
*****
****
***
**
*

Sample Input 2:

+
5

Sample Output 2:

+
++
+++
++
+

Sample Input 3:

?
7

Sample Output 3:

?
??
???
????
???
??
?

def draw_triangle(fill, base):
    flag = False
    center = base // 2 + 1

    for j in range(center, 0, -1):
        if flag == False:
            for i in range(1, center):
                print(fill * i)
            flag = True
        print(fill * j)

# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)
