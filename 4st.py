import math

g=9.8
r=0.2
t=0.1
m=3.6
a=2
n=10

Fhy = (m/n)*((2*g*r*math.tan(math.radians(a)))**0.5/t)
print("所需合力为",Fhy)

