

Напишите программу, которая получает на вход три целых числа, по одному числу в строке, и выводит на консоль в три строки сначала максимальное, потом минимальное, после чего оставшееся число.

На ввод могут подаваться и повторяющиеся числа.

Sample Input 1:

8
2
14

Sample Output 1:

14
2
8

Sample Input 2:

23
23
21

Sample Output 2:

23
21
23



a = int(input())
b = int(input())
c = int(input())
sum = a + b + c
if a > b and a > c and b > c:
    max = a
    print(max, c, b, sep='\n')
elif a > b and a > c and b < c:
    max = a
    print(max, b, c, sep='\n')
elif b > a and b > c and a > c:
    max = b
    print(max, c, a, sep='\n')
elif b > a and b > c and a < c:
    max = b
    print(max, a, c, sep='\n')
elif c > a and c > b and a > b:
    max = c
    print(max, b, a, sep='\n')
elif c > a and c > b and a < b:
    max = c
    print(max, a, b, sep='\n') # Где я?
elif a == b and c > b:
    max = c
    print(max, a, b, sep='\n')
elif a == b and c < b:
    min = c
    print(a, min, b, sep='\n')
elif a == c and b > a:
    max = b
    print(max, a, c, sep='\n')
elif a == c and b < a:
    min = b
    print(a, min, c, sep='\n')
elif b == c and a > b:
    max = a
    print(max, c, b, sep='\n')
elif b == c and a < b:
    min = a
    print(c, min, b, sep='\n')
elif b == c and b == a and a == c:
    print(a, b, c, sep='\n')
