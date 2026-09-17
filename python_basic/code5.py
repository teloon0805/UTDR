import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)  #生成一个随机数生成器对象，使用默认的随机数生成器算法，并设置种子为42，以确保每次运行代码时生成的随机数序列相同。
x = np.linspace(0, 2 * np.pi, 500)
noise = rng.normal(0,0.15,size=x.shape)  #生成一个与x形状相同的随机噪声数组，噪声服从均值为0，标准差为0.15的正态分布。
y = np.sin(x) + noise

plt.plot(x, y, label="noisy signal")

plt.xlabel("time")
plt.ylabel("amplitude")

plt.title("Signal with Noise")

plt.legend()

plt.grid(True)

plt.show()