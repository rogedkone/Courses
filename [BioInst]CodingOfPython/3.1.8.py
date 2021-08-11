Напишите функцию f(x), которая возвращает значение следующей функции, определённой на всей числовой прямой:
f(x)={ 1−(x+2)2,при x≤−2 −x2,при −2<x≤2 (x−2)2+1,при 2<x f(x)= \begin{cases}   1 - (x + 2)^2,\quad &\text{при } x\le -2\\  -\frac x2 ,\quad &\text{при } -2 \lt x \le 2\\   (x-2)^2 + 1,\quad &\text{при } 2 \lt x \end{cases}
f(x)=⎩
⎨
⎧​ 1−(x+2)2, −2x​, (x−2)2+1,​при x≤−2при −2<x≤2при 2<x​

Требуется реализовать только функцию, решение не должно осуществлять операций ввода-вывода.

Sample Input 1:

4.5

Sample Output 1:

7.25

Sample Input 2:

-4.5

Sample Output 2:

-5.25

Sample Input 3:

1

Sample Output 3:

-0.5

def f(x):
	if x <= -2:
		return 1 - (x+2)*(x+2)
	elif -2 < x <= 2:
		return -x/2
	else:
		return (x-2)*(x-2) + 1
