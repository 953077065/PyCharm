import math

g = 9.8     # 重力加速度
t = 0.1     # 假设球接触鼓的时间为0.1s
mq = 0.27   # 排球的重量Kg
mg = 3.6    # 鼓的重量Kg
n = 8       # 8个人

# 降落的高度
hd = 0.4
# 降落的时间
td = (2 * hd / g) ** 0.5
# 降落的末速度
vd = g * td
# 落下后的冲击力
Fd = mq * vd / t
# 弹起的高度
hu = 0.4
# 弹起的时间
tu = (2 * hu / g) ** 0.5
# 弹起的初速度
vu = g * tu
# 弹起的加速度
au = vu / t
# 合力
FM = Fd + mg * g + mq * au
# 绳长
sl = (0.6 / 2) / math.sin(math.radians(180 / n))
# 角度
deg = math.degrees(math.asin(0.11 / sl))
# 分力
FI = FM / n / (0.11 / (sl + 0.2));

print("一共需要的合力为：\t%.2f N" % FM)
print("每人的绳子长度为：\t%.2f M" % sl)
print("每个人的发力方向：\t%.2f °" % deg)
print("每人的发力大小为：\t%.2f N" % FI)
print("此时弹起的高度为：\t%.2f m" % hu)
