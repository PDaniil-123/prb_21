# Не совсем корректная задача, очередь никуда не движется почему то, или некорректный пример
inp = str(input())
aa = inp.split(' ')
n = int(aa[0])  # Бесполезная информация, тоже самое что и длина строки s
t = int(aa[1])
s = str(input())
L = list(s)
for ind in range(0, t):
    print('ind=', ind)
    i = 0
    while i < n - 1:
        if L[i] == 'B' and L[i + 1] == 'G':
            # Была попытка реализации в строчке s=s[:i-1]+'G'+'B'+s[i+2:], но при малых i получались несуществующие индексы
            L[i] = 'G'
            L[i + 1] = 'B'
            i = i + 2
        else:
            i = i + 1
print("".join(L))
