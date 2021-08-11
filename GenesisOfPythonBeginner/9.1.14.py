
Гласные и согласные

На вход программе подается одна строка с буквами русского языка. Напишите программу, которая определяет количество гласных и согласных букв.

Формат входных данных
На вход программе подается одна строка.

Формат выходных данных
Программа должна вывести количество гласных и согласных букв.

Примечание. В русском языке 10 гласных букв (а, у, о, ы, и, э, я, ю, ё, е) и 21 согласная буква (б, в, г, д, ж, з, й, к, л, м, н, п, р, с, т, ф, х, ц, ч, ш, щ).

Sample Input:

Вдохновение – это умение приводить себя в рабочее состояние!

Sample Output:

Количество гласных букв равно 25
Количество согласных букв равно 24

n, gl, sog = input().lower(), 0, 0

for i in n:
    if i in "ауоыиэяюёе":
        gl += 1
    if i in "бвгджзйклмнпрстфхцчшщ":
        sog += 1
print(f"Количество гласных букв равно {gl}")
print(f"Количество согласных букв равно {sog}")
