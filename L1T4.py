inp = str(input())
aa = inp.split(' ')
n = float(aa[0])
t = float(aa[1])
a = input().split(' ')
i = 1
while t > i:
   c=a[int(i-1)]
   print(i)
   i = i + float(c)
if t == i:
    print('Yes')
else:
    print('No')

