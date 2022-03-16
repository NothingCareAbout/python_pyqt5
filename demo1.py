import numpy as np
import random

arr=np.array(range(1,6)) #创建一个数组
arr1=np.arange(1,6) #等价于arr
#print(type(arr))  <class 'numpy.ndarray'>
print(arr1.dtype) #数据类型

arr2=np.array([10*random.random() for i in range(10)])
arr3=np.round(arr2,2) #四舍五入保留2位小数 round(array,n)
print(arr2)
print(arr3)  

