from matplotlib import pyplot as plt
import random

x1=[]
height=0.25
for item in range(1,13):
    x1.append("{}".format(str(item))+"月份")
 
y1=[random.randint(25,60) for i in range(12)]

y2=[random.randint(35,70) for i in range(12)]
fig =plt.figure(figsize=(80,60))

plt.xlabel("月份",loc="right",fontsize=15)
plt.ylabel("票房")

#plt.bar(month,y,width=0.3) #bar 条形图
plt.barh(x1,y1,height=height,label="这是1") #横着的条形图
#plt.barh(month2,y2,height=height,label="这是2") #横着的条形图

plt.title("这是一张条形图")
plt.legend()
#plt.savefig("条形图.png")
plt.show()