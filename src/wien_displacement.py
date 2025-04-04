"""维恩位移定律计算模块

本模块实现了维恩位移定律相关的计算功能，包括：
1. 维恩方程的图像绘制
2. 维恩位移常数的计算
3. 基于维恩位移定律的温度估算

主要函数：
- plot_wien_equation: 绘制维恩方程的图像
- solve_wien_constant: 计算维恩位移常数
- calculate_temperature: 根据波长估算温度
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from scipy import constants

def plot_wien_equation():
    """绘制维恩方程的两个函数图像
    
    绘制方程 5e^(-x) + x - 5 = 0 的图像解释，包括：
    - y = 5e^(-x) 曲线
    - y = 5 - x 直线
    两条曲线的交点即为方程的解
    """
    # TODO: 创建x轴数据点
    # 生成从-1到6的等间距100个点作为x轴数据
    x = np.linspace(-1, 6, 100)
    
    # TODO: 创建图形并设置大小
    
    # TODO: 绘制两条曲线
    
    # TODO: 设置坐标轴标签和标题
    
    # TODO: 添加图例和网格
    
    # TODO: 显示图形
    # 创建8x6英寸大小的画布
    plt.figure(figsize=(8, 6))
    # 绘制红色曲线y=5e^(-x)，并添加图例标签
    plt.plot(x, 5 * np.exp(-x), 'r', label='y = 5 * exp(-x)')
    # 绘制蓝色直线y=5-x，默认颜色，添加图例标签
    plt.plot(x, 5 - x, label='y = 5 - x')
    # 设置x轴和y轴标签
    plt.xlabel('x')
    plt.ylabel('y')
    # 设置图表标题
    plt.title('Graphical Solution of Wien Equation')
    # 在右上角显示图例
    plt.legend()
    # 显示网格线
    plt.grid(True)
    plt.show()

def wien_equation(x):
    """维恩方程：5e^(-x) + x - 5 = 0
    
    参数:
    x (float): 方程的自变量
    
    返回:
    float: 方程的函数值
    """
    # TODO: 返回维恩方程的函数值
    # 返回方程计算结果：5e^(-x) + x -5
    return 5 * np.exp(-x) + x - 5

def solve_wien_constant(x0):
    """求解维恩位移常数
    
    通过求解非线性方程 5e^(-x) + x - 5 = 0 得到 x 值，
    然后计算维恩位移常数 b = hc/(k_B * x)
    
    参数:
    x0 (float): 求解方程的初始值
    
    返回:
    tuple: (x, b)
        - x (float): 非线性方程的解
        - b (float): 维恩位移常数，单位：m·K
    """
    # TODO: 使用fsolve求解非线性方程
    # 使用fsolve求解器，传入方程函数和初始猜测值x0
    x = float(fsolve(wien_equation, x0)[0])                # 提取解并转为浮点数
    
    # TODO: 计算维恩位移常数
    # 计算维恩位移常数：普朗克常数h * 光速c / (玻尔兹曼常数k * 解x)
    b = constants.h * constants.c / (constants.k * x)
    
    return x, b

def calculate_temperature(wavelength, x0=5.0):
    """根据波长计算温度
    
    基于维恩位移定律 λT = b，根据辐射峰值波长计算黑体温度
    
    参数:
    wavelength (float): 峰值波长，单位：米
    x0 (float, optional): 求解方程的初始值，默认为5.0
    
    返回:
    float: 黑体温度，单位：开尔文
    """
    # TODO: 计算温度
    # 获取维恩位移常数b（忽略返回的x值）
    _, b = solve_wien_constant(x0)
    # 根据公式T = b / 波长 计算温度
    return b / wavelength

if __name__ == "__main__":
    # 绘制方程图像
    plot_wien_equation()
    
    # 从键盘输入初值
    try:
        x0 = float(input("请根据图像输入方程求解的初始值（建议值为4-6）："))
    except ValueError:
        print("输入无效，将使用默认值 5")
        x0 = 5
    
    # 计算维恩位移常数
    x, b = solve_wien_constant(x0)
    print(f"\n使用初值 x0 = {x0}")
    print(f"方程的解 x = {x:.6f}")
    print(f"维恩位移常数 b = {b:.6e} m·K")
    
    # 计算太阳表面温度
    # 设定太阳辐射峰值波长（502纳米转换为米）
    wavelength_sun = 502e-9  # 502 nm 转换为米
    # 计算太阳表面温度估计值
    temperature_sun = calculate_temperature(wavelength_sun, x0)
    print(f"\n太阳表面温度估计值：{temperature_sun:.0f} K")
