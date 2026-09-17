import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

x = np.linspace(0, 4 * np.pi, 1000)
clean = np.sin(x)    #干净图形

noise_levels = [0.05, 0.2, 0.5]    #扰动强度

fig, axes = plt.subplots(3, 1, figsize=(10, 8))   #subplots函数返回两个结果，fig整体，axes数组（包括每个子图）

for ax, noise_level in zip(axes, noise_levels):    #zip打包操作，把axes和noise_levels打包成一个元组列表
    noise = rng.normal(0, noise_level, size=x.shape)
    noisy = clean + noise

    print(
        "噪声强度:",
        noise_level,
        "均值:",
        noisy.mean(),
        "标准差:",
        noisy.std()
    )

    ax.plot(x, noisy)
    ax.set_title(f"Noise level = {noise_level}")
    ax.grid(True)

plt.tight_layout()       #自动排版
plt.show()