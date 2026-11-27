# 首页排版与素材

[返回首页](../README.md)

## 海洋蓝配色

2026-11-26 记录：后续学习图示以蓝色系、海洋色系为主。

| 用途 | 颜色 | 色值 |
| --- | --- | --- |
| 标题、正文与起点 | 深海蓝 | `#153B57` |
| 主强调色 | 海洋蓝 | `#1D6FA5` |
| 辅助强调色 | 青蓝 | `#1685A8` |
| 第二组对照 | 深蓝 | `#285FA3` |
| 次要曲线 | 浅海蓝 | `#7AAAC6` |
| 背景 | 浅蓝白 | `#F4F9FD` |

同一张图尽量使用两三种主要颜色。不同情况同时用实线、虚线、圆点、菱形或文字区分，保持缩小后可读。照片优先选择海洋观测实拍；灰度数组等具有数值含义的图保留原有数据映射。

## 排版

首页从个人起点与当前进度展开，随后说明识别、检测和学习顺序，最后回到已有成果和计划中的作品。顶部导航用于跳转，维护命令和目录收进折叠区，方便以后持续增长。

照片围绕具体的视觉观察问题选取。灰度裁剪保留为一次播放的教学动画；真实模型结果完成后，再放入成果区。

## 摄影

三张照片均来自 NOAA Fisheries 的 [Sea Tales of Deep Dives and Shallow Reefs](https://www.fisheries.noaa.gov/science-blog/sea-tales-deep-dives-and-shallow-reefs)，保留原始下载文件，仅通过页面布局缩放显示。照片用于学习主页的配图与观察说明，未添加预测框，不是实验输出。

| 仓库文件 | 内容与署名 | 原始图片 |
| --- | --- | --- |
| [baker-reef.jpg](../assets/images/baker-reef.jpg) | 贝克岛珊瑚礁上的鱼群；Jeffrey Milisen / NOAA Fisheries | [NOAA 图片](https://media.fisheries.noaa.gov/dam-migration-miss/1280_cF5Y6JgPfN56.jpg?1529357483=) |
| [goby-camouflage.jpg](../assets/images/goby-camouflage.jpg) | 与海底砂砾颜色相近的虾虎鱼；Louise Giuseffi / NOAA Fisheries | [NOAA 图片](https://media.fisheries.noaa.gov/dam-migration-miss/1280_cyH4DbhdKpg5.jpg?1531174851=) |
| [swains-fish.jpg](../assets/images/swains-fish.jpg) | 斯温斯岛附近的黑鳍梭鱼群；Jeff Milisen / NOAA Fisheries | [NOAA 图片](https://media.fisheries.noaa.gov/dam-migration-miss/1280_Y5ZBy3BPjW97.jpg?1529708905=) |

使用依据：[NOAA Fisheries 图片与版权政策](https://www.fisheries.noaa.gov/national/about-us/website-policies-and-disclaimers#copyright-policy)。图片按原文署名；引用不代表 NOAA 对本项目的认可。

## 动画与字体

裁剪动图取自第一课的灰度数组，播放一次后停在最后一帧。相同内容可查看[静态图](../assets/images/array-crop.png)，生成代码见 [build_visuals.py](../scripts/build_visuals.py)。

动图使用 DM Mono 字体。[字体许可](../assets/fonts/DMMono-OFL.txt)

## 损失曲线教学图

[参数与损失图](../assets/images/parameter-loss.png)由公式 `L = (2w - 6)²` 生成。两幅图使用相同坐标范围，对比从同一个起点进行不同幅度的参数调整，属于单样本教学示意，不是实际训练曲线。

[梯度方向图](../assets/images/gradient-direction.png)沿用同一公式，标出两个位置的切线以及减小损失的局部更新方向，用圆点与菱形辅助区分。

生成代码见 [plot_parameter_loss.py](../scripts/plot_parameter_loss.py)，依赖 matplotlib（已列在 [numpy_basic/requirements.txt](../numpy_basic/requirements.txt)），中文标签使用系统中文字体，如微软雅黑或 Noto Sans CJK SC。

```powershell
python scripts/plot_parameter_loss.py
```
