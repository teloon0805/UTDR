import numpy as np
import matplotlib.pyplot as plt

image = np.random.default_rng(42).random((100, 150))  #生成一个100x150的随机图像，像素值在0到1之间均匀分布。

plt.imshow(image, cmap="gray")
plt.colorbar()
plt.title("A 2D Array")
plt.show()