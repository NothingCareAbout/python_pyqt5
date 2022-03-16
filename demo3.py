from cProfile import label
from turtle import color
from matplotlib import pyplot as plt
import random

from pyparsing import alphanums

x=range(12,25,1)

y1=[random.randint(10,20) for i in range(13)]
y2=[random.randint(15,25) for i in range(13)]
y3=[random.randint(30,45) for i in range(13)]

plt.plot(x,y1,label="这是我")
plt.plot(x,y2,label="这是他")  #绘制折线图

plt.grid(alpha=0.4)  #添加轴线  ,alpha 设置轴线透明度
plt.legend() #添加图例 loc指定位置
plt.savefig("demo3.png")

plt.scatter(x,y3)   #scatter 绘制散点图



plt.show()