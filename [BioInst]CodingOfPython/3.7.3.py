

Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
Если введённое слово не найдено в этом списке, оно помечается как "ошибка".

Попробуем написать подобную систему.

На вход программе первой строкой передаётся количество d d d известных нам слов, после чего на d d d строках указываются эти слова. Затем передаётся количество l l l строк текста для проверки, после чего l l l строк текста.

Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.

Sample Input:

4
champions
we
are
Stepik
3
We are the champignons
We Are The Champions
Stepic

Sample Output:

stepic
champignons
the

known = set()
unknown = set()

for _ in range(int(input())):
    known.add(input().strip().lower())

for _ in range(int(input())):
    for word in input().strip().lower().split():
        if word not in known:
            unknown.add(word)

for word in unknown:
    print(word)
