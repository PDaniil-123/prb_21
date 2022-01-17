from math import cos, acos, sqrt, pi, sin, asin

R = 6371001
r0 = 25
point = ['60.051584', '30.300509']
y0 = float(point[0]) * pi / 180  # широта  Lat
u0 = float(point[1]) * pi / 180  # долгота Lon
f = open('nmea.log', 'r')
content = f.read()
content = content.splitlines(True)
table = [content[0].split(',')]
n = 0
t = 0
for l in range(1, len(content)):
    if len(content[l].split(',')) == 15:
        table = table + [content[l].split(',')]
for i in range(len(table) - 1):
    yi = (float(table[i][2][0:2]) + float(table[i][2][2:]) / 60) * pi / 180
    ui = (float(table[i][4][0:3]) + float(table[i][4][3:]) / 60) * pi / 180
    delta = acos(sin(yi) * sin(y0) + cos(yi) * cos(y0) * cos(u0 - ui))
    dist = R * delta
    if dist < r0:
        dt = round(float(table[i + 1][1]) - float(table[i][1]), 1)
        # интервал измерений непостоянный, имеются значительные паузы, в которых непонятно где находится прибор
        t = t + dt
        n = n + 1
dt = round(float(table[1][1]) - float(table[0][1]), 1)
print(n,'точек')  # Количество точек, в котором прибор был на нужном расстоянии.
print(n * dt / 60, 'm')
print(round(t / 60, 2), 'm')
f.close
