Катя узнала, что ей для сна надо X X X минут. В отличие от Коли, Катя ложится спать после полуночи в H H H часов и M M M минут. Помогите Кате определить, на какое время ей поставить будильник, чтобы он прозвенел ровно через X X X минут после того, как она ляжет спать.

На стандартный ввод, каждое в своей строке, подаются значения X X X, H H H и M M M. Гарантируется, что Катя должна проснуться в тот же день, что и заснуть. Программа должна выводить время, на которое нужно поставить будильник: в первой строке часы, во второй — минуты.

Sample Input 1:

480
1
2

Sample Output 1:

9
2

Sample Input 2:

475
1
55

Sample Output 2:

9
50

x = int(input())  # Указываем минуты для сна
h = int(input())  # Указываем текущие часы
m = int(input())  # Указываем текущие минуты
i = x + ((h * 60) + m)  # общее время = мин_сна + (Часы(в минутах)+минуты)


print(i // 60)  # Ищем от общего времени количество часов
print(i % 60)  # Ищем от общего времени количество минут
