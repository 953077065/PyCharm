import math

# 鼓面位置编号 逆时针方向
# 7 6 5 4
# 0 1 2 3
# 相对面 0-4 1-5 2-6 3-7
force = []
for i in range(8):
    force.append(float(input("请输入第%d个发力大小:" % (i + 1))))
# time = []
# for i in range(8):
#     time.append(float(input("请输入第%d个发力时间:" % (i + 1))))
print("发力大小为：", end="\t")
for i in force:
    print(i, end="\t")
# print("\n发力时间为：", end="\t")
# for i in time:
#     print(i, end="\t\t")
print()
# 判断数组
if force[0] == force[4]:
    force[0] = 0
    force[4] = 0
if force[1] == force[5]:
    force[1] = 0
    force[5] = 0
if force[2] == force[6]:
    force[2] = 0
    force[6] = 0
if force[3] == force[7]:
    force[3] = 0
    force[7] = 0
print("处理后大小为：", end="\t")
for i in force:
    print(i, end="\t")
# 合力计算
deg = 0
# 夹角个数，一个为45° 先判断是否有2个非0数，在判断其中间是否有0
# 如果有0 则夹角为（0的个数+1）* 45°，如果没0 夹角为45度
flag = 0
# 标记 是否2个非0数的标记
flg = 0
# 非0 个数
num = []
for i in range(4):
    if force[i] != 0.0:
        flag += 1
        num.append(i)
# 大于一个非0数的处理
if flag > 1:
    # 先判断中间夹的几个0
    i = num[0]
    while i < num[-1]:
        if force[i] == 0:
            flg += 1
        i += 1
    deg = (flg + 1) * 45
    # 夹角
    f1 = abs(force[num[0]] - force[num[0] + 4])
    f2 = abs(force[num[1]] - force[num[1] + 4])
    # 第一种算法 假设2个力相等
    Fh = 2 * f1 * math.cos(math.radians(deg / 2))
    # 第二种算法 2个力不等 未完成,不能用
    # Fh = (2*f1**2+2*f2**2-(f1**2+f2**2-2*f1*f2*math.cos(math.radians(deg)))**2)*0.5
# 只有1个非0数的处理
else:
    Fh = abs(force[num[0]] - force[num[0] + 4])
print()
print("合力为", Fh)
g = 9.8  # g
r = 0.2  # 鼓半径
sg = 0.11  # 绳高
sc = 1.7  # 绳长
m = 3.6 / 8 # 鼓的质量
t = 0.1  # 接触时间
# 合力分力
Fhy = Fh * sg / sc
print("Fhy:\t",Fhy)
# Fhy = ma a=>加速度
a = Fhy / m
print("\ta:\t",a)
# v=at v 鼓上升瞬时速度
v = a * t
print("\tv:\t",v)
# mgh=1/2*v^2*m h=>高度
h = v ** 2 / (2 * g)
print("\th:\t",h)
# 角度tanx=h/r
degree = math.degrees(math.atan(h / r))

print("Degree:\t", degree)
