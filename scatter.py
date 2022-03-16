
from matplotlib import pyplot as plt
import random
x=range(12,25,1)
y=[random.randint(30,45) for i in range(13)]

fig=plt.figure(figsize=(100,60),dpi=80)

plt.grid(alpha=0.4)  #添加轴线  ,alpha 设置轴线透明度
#plt.legend() #添加图例 loc指定位置
plt.title("这是一张散点图")
plt.scatter(x,y)   #scatter 绘制散点图
plt.savefig("散点图.png")

plt.show()
