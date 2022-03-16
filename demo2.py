from matplotlib import pyplot as plt
import random


x=range(120) 
y=[random.randint(20,35) for i in range(120)]

fig=plt.figure(figsize=(100,60))
plt.title("人效")

x_ticks=x[::3]

plt.xticks(x_ticks,rotation=90)

plt.plot(x,y)

plt.show()