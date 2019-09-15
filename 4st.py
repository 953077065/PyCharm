import math

g = 9.8
r = 0.2
t = 0.1
m = 3.6
a = 2
n = 10
sc = 2
sg = 0.11

Fhy = (m / n) * ((2 * g * r * math.tan(math.radians(a))) ** 0.5 / t)
print("所需合力为", Fhy)

Fh = Fhy / (sg / sc)
print("绳子拉力为", Fh)

f1 = math.cos(math.radians(12)) * Fh
f2 = math.cos(math.radians(24)) * Fh
print("用力大小", f1, f2)
