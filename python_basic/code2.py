import numpy as np

a=np.array([1,2,3,4,5,6])

print("数组：",a)
print("数组形状：",a.shape)
print("数组维度：",a.ndim)
print("数组数据类型：",a.dtype)

b = a.reshape(2,3)

print("二维数组：")
print(b)
print("第一行：",b[0])
print("第二行：",b[:,1])