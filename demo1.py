import pandas as pd
from  matplotlib import pyplot as plt
#plt.rcParams["font.sans-serif"]=["SimHei"] #设置字体
#plt.rcParams["axes.unicode_minus"]=False #该语句解决图像中的“-”负号的乱码问题

fig=plt.figure("hahh",figsize=(80,40),dpi=60) #figure 图表

plt.xlabel("时间",fontsize="20",color="blue")  #xlabel x轴标签
plt.ylabel("温度",fontsize="20")

x=range(2,26,2)
y=[17,26,25,30,15,48,23,48,15,35,26,24]
x_tick=[]
for i in range(2,49,2):
    x_tick.append(i/2)

plt.xticks(x_tick) #x轴的刻度大小 要和x个数一一对应

plt.plot(x,y)

plt.title("气温变化图",fontsize="30")

#plt.savefig("firstfig.png")

plt.show()