# -*- coding: UTF-8 -*-
__author__ = 'aerpyljov'

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
