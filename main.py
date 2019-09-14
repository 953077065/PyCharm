g = 9.8 #重力加速度
t = 0.1 #假设球接触鼓的时间为0.1s
mq = 0.27 #排球的重量Kg
mg = 3.6 #鼓的重量Kg

#降落的高度
hd = 0.4
#降落的时间
td = (2*hd/g)**0.5
#降落的末速度
vd = g * td
#落下后的冲击力
Fd = mq*vd/t

print("第一次降落的时间为：\t",td)
print("第一次降落的末速度：\t",vd)
print("第一次降落冲击力为：\t",Fd)
#弹起的高度
hu = 0.4
#弹起的时间
tu = (2*hu/g)**0.5
#弹起的初速度
vu = g*tu
#弹起的加速度
au = vu/t
#合力
FM = Fd+mg*g+mq*au
print("第一次弹起的时间为：\t",tu)
print("第一次弹起初速度为：\t",vu)
print("第一次弹起瞬间加速度：\t",au)
print("第一次需要合力为\t\t",FM)

Fu=FM-mg*g;
au=(Fu-Fd)/mq;
vu=au*t;
tu=vu/g;
hu=tu*tu*g/2;
print("第一次弹起的时间为：\t",tu);
print("第一次弹起的初速度为：\t",vu);
print("第一次弹起瞬间加速度：\t",au);
print("第一次需要的弹力为：\t",Fu);
print("第一次需要人的合力为：\t",FM);
print("第一次弹起的距离为：\t",hu);
