from email import contentmanager
import numpy as np
import random
import re

lst=[random.randint(10000,12354) for i in range(1000)]

arr=np.array((lst)).reshape(250,4)
index=0
while index<250:
    item=arr[index]
    content=str(item)
    text=content.replace(" ",",")
    t1=text.strip("[")
    t2=t1.strip("]") #strip 删除首尾指定的字符   
    filename=r"D:\Python\pandas\numpy\exercise.txt"
    with open (filename,"a") as f:
        f.writelines(t2+"\n")
    index+=1