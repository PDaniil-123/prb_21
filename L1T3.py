print('Введите строку')
c = str(input())
i = 0
for n in range(0, len(c)):
    if c.count(c[n]) == 1:
        i = i + 1
print('Уникальных символов в строке', i)
