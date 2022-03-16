from matplotlib import pyplot as plt
import random

lst=[random.randint(10,150) for i in range(200)]
fig=plt.figure(figsize=(100,80))

组距=5

组数=(max(lst)-min(lst))//组距

plt.xticks(range(min(lst),max(lst)+组距,组距))

plt.hist(lst,组数,(100,150))  #hist 直方图 (100,150) 范围
plt.savefig("直方图.png")
plt.show()
