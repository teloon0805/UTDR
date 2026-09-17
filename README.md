# Underwater Perception Lab

> 水下目标识别与检测一体化学习与研究记录

[![Status](https://img.shields.io/badge/status-learning%20in%20progress-1f6feb?style=flat-square)](#学习路线)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-planned-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)](https://pytorch.org/)

这是一个面向初学者的长期学习型项目，记录从 Python、科学计算和深度学习基础，到水下光学感知、声呐信号处理、多模态融合与目标跟踪的完整过程。

项目以公开数据、公开代码和可复现实验为主，聚焦于公开水下场景中的目标检测、识别、跟踪与环境鲁棒性。

---

## 项目目标

水下感知与陆地图像识别存在明显差异：

- 光学图像受到吸收、散射、色偏、低照度和浑浊水体影响；
- 声呐数据受到传播损失、多径、混响、散斑噪声和低信噪比影响；
- 光学与声呐的数据分布、时间尺度和空间坐标并不天然一致；
- 真实水下数据获取成本高，训练数据和实际海况之间往往存在域差异。

本项目希望逐步回答三个问题：

1. 如何在水下退化条件下稳定检测目标？
2. 如何结合光学和声呐信息提升目标识别的可靠性？
3. 当某个传感器失效、环境变化或出现未知目标时，系统如何保持可用？

## 学习路线

```text
Python / Linux / Git
          ↓
数学、概率与统计
          ↓
NumPy / Matplotlib / PyTorch
          ↓
CNN、迁移学习与目标检测
          ↓
水下光学成像与图像增强
          ↓
信号与系统、FFT、STFT
          ↓
水声学、声呐与阵列信号处理
          ↓
目标跟踪、跨模态融合与开放集识别
          ↓
公开数据复现 → 对照实验 → 独立研究问题
```

### 24周路线图

| 阶段 | 学习内容 | 阶段产出 |
| --- | --- | --- |
| 编程与工具 | Python、NumPy、Matplotlib、Git、虚拟环境 | 可复用的基础代码与实验日志 |
| 数学与深度学习  | 线性代数、概率、梯度、PyTorch、CNN、迁移学习 | MNIST/CIFAR分类器、训练模板 |
| 计算机视觉  | IoU、NMS、mAP、YOLO、自定义数据集 | 第一个水下图像检测基线 |
| 水下光学  | 吸收、散射、色偏、增强与域变化 | 原图/增强图/模型的对照报告 |
| 信号与水声  | 采样、滤波、FFT、STFT、水声传播、声呐、CFAR | 声信号分析和声呐检测基线 |
| 融合与选题  | 光学+声呐融合、ByteTrack、卡尔曼滤波 | 研究问题、数据、基线与实验计划 |

路线中的每一阶段都遵循：

```text
概念理解 → 小实验 → 开源基线 → 误差分析 → 论文阅读 → 可复现实验
```


## 第一阶段：基础学习计划

### Python、NumPy 与 Matplotlib

目标：能够独立读取、处理、统计和可视化数组数据。

- Python：变量、列表、字典、循环、函数和文件读写；
- NumPy：数组、维度、形状、索引、切片、变形、广播和统计；
- Matplotlib：折线图、散点图、直方图和二维矩阵显示；
- 小项目：生成带噪声的信号，比较不同噪声强度下的均值、标准差和图形变化。

### Git、Linux 与实验管理

目标：让每一次实验都能被记录、复查和复现。

- 使用虚拟环境管理依赖；
- 用 Git 保存代码和实验版本；
- 为每个实验记录数据、参数、指标、硬件和结论；
- 练习从一个干净环境重新运行项目。

### 机器学习与深度学习基础

目标：理解模型如何学习，而不只是调用训练命令。

- 线性代数、概率统计和梯度下降；
- PyTorch 张量、数据集、数据加载器、训练与验证；
- CNN、BatchNorm、残差连接、过拟合与数据增强；
- 使用预训练 ResNet 完成小数据集分类。

### 目标检测与 YOLO

目标：建立一个可信的水下视觉检测基线。

- 理解边界框、类别、IoU、NMS、Precision、Recall 和 mAP；
- 阅读 YOLO 方法论文，运行官方示例；
- 使用 CVAT 标注小型水下数据集；
- 比较原图、增强图和不同模型的检测结果。

### 水下与声呐

目标：从“图像检测”扩展到“水下传感器感知”。

- 水下光学：吸收、散射、色偏、低照度和图像增强；
- 信号处理：采样、卷积、相关、滤波、FFT、STFT；
- 水声学：声速、传播损失、多径、混响和 Doppler；
- 声呐：主动/被动声呐、侧扫声呐、前视声呐、波束形成和 CFAR；
- 融合：光学与声呐的后期融合、质量感知融合和模态缺失测试。

## 建议资源

### 学习课程与文档

- [动手学深度学习](https://d2l.ai/)
- [PyTorch Tutorials](https://pytorch.org/tutorials/)
- [NumPy Quickstart](https://numpy.org/doc/stable/user/quickstart.html)
- [Matplotlib Quick Start](https://matplotlib.org/stable/users/explain/quick_start.html)
- B站搜索：`Python基础`、`NumPy`、`Matplotlib`、`PyTorch`、`数字信号处理`、`水声学`、`目标检测 YOLO`

### 书籍方向

- 编程与数据分析：《Python编程：从入门到实践》《利用Python进行数据分析》
- 机器学习：《机器学习》《统计学习方法》
- 深度学习：《深度学习》
- 信号与水声：《信号与系统》《数字信号处理》《水声学原理》《阵列信号处理》

### 开源工具

- [Ultralytics](https://github.com/ultralytics/ultralytics)：YOLO训练与推理
- [MMDetection](https://github.com/open-mmlab/mmdetection)：目标检测基准
- [CVAT](https://github.com/cvat-ai/cvat)：数据标注
- [Albumentations](https://github.com/albumentations-team/albumentations)：图像增强
- [ByteTrack](https://github.com/ifzhang/ByteTrack)：多目标跟踪
- [SUIM](https://github.com/xiaosean/SUIM)：水下图像分割
- [arlpy](https://github.com/org-arl/arlpy)：水声和阵列信号处理

## 计划使用的数据

### 光学数据

优先考虑 SUIM、UIEB、TrashCan、DUO、URPC 相关数据集和 Brackish Dataset。使用前会核对许可证、标注格式和数据划分方式。

### 声呐数据

优先寻找公开的前视声呐、侧扫声呐、声呐图像分类和水下声学目标识别数据。真实场景数据通常难以规模化获取，因此研究将使用公开目标、仿真数据或合规采集数据。

## 实验规范

每个实验至少记录以下内容：

| 项目 | 记录内容 |
| --- | --- |
| 数据 | 数据集版本、许可证、训练/验证/测试划分 |
| 环境 | Python、CUDA、GPU、主要依赖版本 |
| 方法 | 模型、预训练权重、输入尺寸和数据增强 |
| 参数 | 学习率、batch size、epoch、随机种子 |
| 指标 | Precision、Recall、F1、mAP、FPS、参数量 |
| 结果 | 最优结果、均值/标准差、失败样本 |
| 结论 | 哪个因素有效、哪里失效、下一步怎么改 |

特别注意：视频数据应按“场景或视频”划分，而不是把相邻帧随机分到训练集和测试集，以避免数据泄漏。

## 预期研究问题

后续会从以下方向中选择一个形成正式课题：

1. **质量感知的光学-声呐融合**：根据图像清晰度和声呐信噪比动态调整模态权重；
2. **模态缺失下的水下检测**：某个传感器不可用时保持检测性能；
3. **跨海况域适应**：研究模型从清水到浑浊水域的迁移；
4. **水下小目标检测与跟踪**：面向远距离、低对比度目标；
5. **开放集识别**：识别已知目标，同时发现训练集之外的未知目标。

当前优先方向：

> 面向复杂水下环境的质量感知光学-声呐多模态目标检测方法研究

## 持续更新

这个仓库会持续记录：

- 每周学习目标与完成情况；
- 代码、配置和运行结果；
- 论文阅读卡片与复现报告；
- 失败案例、错误分析和改进尝试；
- 阶段性研究问题和实验结论。

更新格式示例：

```text
日期：2026-09-17
阶段：Week 1 / NumPy
完成：数组创建、reshape、切片
输出：lesson2.py
问题：需要进一步理解广播机制
下一步：完成Matplotlib二维数组可视化
```

## 免责声明

本项目用于公开的水下感知、信号处理和机器学习研究，涉及的目标检测、识别与跟踪方法面向学术学习和公开场景验证。

---

如果你也在学习水下感知、声呐信号处理或目标检测，欢迎通过 Issue 交流公开资料、复现实验和改进建议。
