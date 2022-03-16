from struct import unpack
import numpy as np

#csv_file=r"D:\Python\pandas\numpy\exercise .csv"


#arr=np.loadtxt(csv_file,delimiter=",",dtype='int') #delimiter 对字符串分割处理
#arr2=arr.transpose() #转置 等价于arr.T
#arr1=np.loadtxt(csv_file,delimiter=",",unpack=True) #unpack=true 转置

#对数据处理操作
#取不连续的多行
#lines=arr[[20,45,36,48]]# [20,45,36,48] 表示取20 45 36行
#print(lines)
##取列数

#colu=arr[:,0]  #取第一列

#colu1=arr[2:,1] #从第三行开始，取第二列

#colu2=arr[:,[0,2]] #取第一和第三列

#取任意行和任意列交叉位置的值

#rcs=arr[[20,30],[1,3]] #row 21 和column 2的交叉点 31和4交差点
#print(rcs)


#对numpy内的数据进行修改
#arr[:,0:3]=0 将第一个和第三列值替换为0
#将小于某一数的值都替换为某一值
#print(arr<11950) #返回的是bool索引 

#arr[arr<11950]=20000  #将小于某一数的值都替换为某一值

#print(arr)
#np.where (arr<value,value1,value2) 三元运算符/
# 如果值小于value将True的索引位置处值都替换为value1否则替换为value2
#np.clip(v1,v2) 将小于v1的值替换为v1 ，大于v2的值替换为v2，中间值为nan 


#数据的拼接

t1=np.arange(1,21).reshape(4,5)
t2=np.arange(22,42).reshape(4,5)
print(t1)
print("---------------------")
print(t2)
print("---------------------")
t3=np.vstack((t1,t2)) #竖直拼接
print(t3)
print("---------------------")
t4=np.hstack((t1,t2)) #水平拼接
print(t4)

