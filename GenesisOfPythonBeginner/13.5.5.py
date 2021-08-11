
Good password 🌶️

Напишите функцию is_password_good(password), которая принимает в качестве аргумента строковое значение пароля password и возвращает значение True если пароль является надежным и False в противном случае.

Пароль является надежным если:

    его длина не менее 888 символов; 
    он содержит как минимум одну заглавную букву (верхний регистр); 
    он содержит как минимум одну строчную букву (нижний регистр);
    он содержит хотя бы одну цифру.

 Примечание. Следующий программный код:

print(is_password_good('aabbCC11OP'))
print(is_password_good('abC1pu'))

должен выводить:

True
False

def is_password_good(password):
    if len(password) < 8:
        return False
    if password in (password.lower(), password.upper()):
        return False
    for c in password:
        if c.isdigit():
            break
    else:
        return False
    return True

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))
