import math
import numpy



g = 9.8  # g
r = 0.2  # 鼓半径
Fh = float(input("输入合力"))  # 合力
sg = 0.11  # 绳高
sc = 1.7  # 绳长
m = 3.6  # 鼓的质量
t = 0.1  # 接触时间
# 合力分力
Fhy = Fh * sg / sc
# Fhy = ma a=>加速度
a = Fhy / m
# v=at v 鼓上升瞬时速度
v = a * t
# mgh=1/2*v^2*m h=>高度
h = v ** 2 / 2 * g
# 角度tanx=h/r
degree = math.degrees(math.atan(h / r))

print("角度是", degree)
