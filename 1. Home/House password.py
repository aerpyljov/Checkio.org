# -*- coding: UTF-8 -*-

'''
http://www.checkio.org/mission/house-password/


Стефан и София забывают о безопасности и используют простые пароли для всего.
Помогите Николе разработать модуль для проверки паролей на безопасность.
Пароль считается достаточно стойким, если его длина больше или равна 10 символам, он содержит, как минимум одну цифру, одну букву в верхнем и одну в нижнем регистре.
Пароль может содержать только латинские буквы и/или цифры.

Вх. данные: Пароль как строка (str, unicode).

Вых. данные: Безопасность пароля в виде булевого значения (bool) или любого типа данных, который может быть сконвертирован и представлен как булево значение (True или False)

Example:

checkio('A1213pokl') == False

checkio('bAse730onE') == True

checkio('asasasasasasasaas') == False

checkio('QWERTYqwerty') == False

checkio('123456123456') == False

checkio('QwErTy911poqqqq') == True



Как это используется: Если вы беспокоитесь о безопасности вашего приложения или сервиса, вы можете проверять пароли ваших пользователей на "сложность".
Также вы можете использовать свои навыки и усложнить требования к паролям.

Предусловия:
re.match("[a-zA-Z0-9]+", password)
0 < len(password) ≤ 64
'''



def password_len(password):
    min_len = 10
    if len(password) >= min_len:
        return True
    else:
        return False


def password_upper_letter(password):
    if password == password.lower():
        return False
    else:
        return True


def password_lower_letter(password):
    if password == password.upper():
        return False
    else:
        return True


def password_digits(password):
    for char in password:
        if char in '0123456789':
            return True
    return False


def checkio(password):
    test1 = password_len(password)
    test2 = password_upper_letter(password)
    test3 = password_lower_letter(password)
    test4 = password_digits(password)
    return (test1 and test2 and test3 and test4)







print (checkio('A1213pokl') == False)

print (checkio('bAse730onE') == True)

print (checkio('asasasasasasasaas') == False)

print (checkio('QWERTYqwerty') == False)

print (checkio('123456123456') == False)

print (checkio('QwErTy911poqqqq') == True)
