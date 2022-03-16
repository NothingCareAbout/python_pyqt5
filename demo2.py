import numpy as np
import random

arr=np.array([[random.randint(3,6) for i in range(10)],[random.randint(6,8) for i in range(10)]])

print(arr.shape) #二维数组

print(arr.shape[0])
print("-------------------------")
arr1=np.array(range(24)).reshape(2,3,4)
arr4=arr1.flatten() #拍平

arr3=arr1.shape[0]

print(arr1) #三维数组

print(arr4) #

###数组的计算？
arr5=np.array(range(24)).reshape(2,3,4)+2 # 每个元素都加了2 加减乘除一样的

print(arr5) 


