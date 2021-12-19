print('Введите строку')
c = str(input())
if c == c[::-1]:
    print('Это палиндромом')
else:
    print('Это не палиндромом')
