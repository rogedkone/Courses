Удали меня полностью

На вход программе подается строка текста. Напишите программу, которая удаляет все вхождения символа «@».

Формат входных данных 
На вход программе подается строка текста.

Формат выходных данных
Программа должна вывести текст в соответствии с условием задачи.

Sample Input 1:

123@1@@34

Sample Output 1:

123134

Sample Input 2:

@@

Sample Output 2: 
  
  n = input()

print(n.replace("@", ""))
