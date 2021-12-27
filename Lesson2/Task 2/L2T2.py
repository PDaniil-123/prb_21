# https://codeforces.com/problemset/problem/230/B
n = int(input())
inp = str(input()).split(' ')
for i in range(0, n):
    iii = 0
    for ii in range(1, int(inp[i])+1):
        if int(inp[i]) % ii == 0:
            iii = iii + 1
    if iii == 3:
        print('YES')
    else:
        print('NO')
