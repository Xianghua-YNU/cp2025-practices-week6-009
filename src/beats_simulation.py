import numpy as np
import matplotlib.pyplot as plt

def simulate_beat_frequency(f1=440, f2=444, A1=1.0, A2=1.0, t_start=0, t_end=1, num_points=5000, show_plot=True):
#show_plot=True 是一个默认参数，它的作用是：控制是否自动显示绘图：当设为 True 时（默认值），函数会自动弹出波形可视化窗口；设为 False 时，只计算数据不显示图形。
    """
    任务1: 拍频现象的数值模拟
    参数说明:
        f1, f2: 两个波的频率(Hz)
        A1, A2: 两个波的振幅
        t_start, t_end: 时间范围(s)
        num_points: 采样点数
    """
    # 学生任务1: 生成时间范围
    t = np.linspace(t_start, t_end, num_points)
    
    # 学生任务2: 生成两个正弦波
    wave1 = A1 * np.sin(2 * np.pi * f1 * t)
    wave2 = A2 * np.sin(2 * np.pi * f2 * t)
    
    # 学生任务3: 叠加两个波
    superposed_wave = wave1 + wave2

    # 学生任务4: 计算拍频
    beat_frequency = abs(f1 - f2)

    # 学生任务5: 绘制图像
    if show_plot:
        plt.figure(figsize=(12, 6))
        
        # 绘制第一个波
        plt.subplot(3, 1, 1)#绘制三行一列的子图，这是第一个图
        # 学生任务6: 完成wave1的绘制
        plt.plot(t, wave1, 'b-', linewidth=1, label=f'频率{f1}Hz, 振幅{A1}')#蓝色实线，粗细为1
        plt.title('第一个正弦波')
        plt.ylabel('振幅')
        plt.legend()#图例
        plt.grid(True)#网格
        
        # 绘制第二个波
        plt.subplot(3, 1, 2)
        # 学生任务7: 完成wave2的绘制
        plt.plot(t, wave2, 'r-', linewidth=1, label=f'频率{f2}Hz, 振幅{A2}')
        plt.title('第二个正弦波')
        plt.ylabel('振幅')
        plt.legend()
        plt.grid(True)
        
        # 绘制叠加波
        plt.subplot(3, 1, 3)
        # 学生任务8: 完成superposed_wave的绘制
        plt.plot(t, superposed_wave, 'g-', linewidth=1, label=f'叠加波形, 拍频{beat_frequency}Hz')
        plt.title('叠加后的波形(拍频现象)')
        plt.xlabel('时间(s)')
        plt.ylabel('振幅')
        plt.legend()
        plt.grid(True)
        
        plt.tight_layout()#优化布局，防止图像重叠
        plt.show()

    return t, superposed_wave, beat_frequency

def parameter_sensitivity_analysis():
    """
    任务2: 参数敏感性分析
    需要完成:
    1. 分析不同频率差对拍频的影响
    2. 分析不同振幅比例对拍频的影响
    """
    # 学生任务9: 频率差分析
    plt.figure(1, figsize=(12, 8))
    # 学生需要在此处添加频率差分析的代码
    base_freq = 440  # 基准频率
    delta_fs = [1, 2, 5, 10, 20]  # 不同的频率差
    t = np.linspace(0, 1, 5000)#生成5000个时间点
    
    for i, delta_f in enumerate(delta_fs):
        f2 = base_freq + delta_f
        wave1 = np.sin(2 * np.pi * base_freq * t)#不改变频率的原波
        wave2 = np.sin(2 * np.pi * f2 * t)#改变频率后的波
        superposed_wave = wave1 + wave2
        
        plt.subplot(len(delta_fs), 1, i+1)
        plt.plot(t, superposed_wave, label=f'f1=440Hz, f2={f2}Hz, 拍频={delta_f}Hz')
        plt.ylabel('振幅')
        plt.legend()
        plt.grid(True)
        if i == len(delta_fs)-1:
            plt.xlabel('时间(s)')
    
    plt.suptitle('不同频率差对拍频现象的影响')
    plt.tight_layout()
    
    # 学生任务10: 振幅比例分析
    plt.figure(2, figsize=(12, 8))
    # 学生需要在此处添加振幅比例分析的代码
    f1, f2 = 440, 444  # 固定频率
    amp_ratios = [1.0, 0.8, 0.5, 0.3, 0.1]  # 振幅比例(A2/A1)
    
    for i, ratio in enumerate(amp_ratios):
        A1 = 1.0
        A2 = A1 * ratio    #改变后的频率
        wave1 = A1 * np.sin(2 * np.pi * f1 * t)
        wave2 = A2 * np.sin(2 * np.pi * f2 * t)
        superposed_wave = wave1 + wave2
        
        plt.subplot(len(amp_ratios), 1, i+1)
        plt.plot(t, superposed_wave, label=f'A1={A1}, A2={A2:.1f}, 比例={ratio:.1f}')
        plt.ylabel('振幅')
        plt.legend()
        plt.grid(True)
        if i == len(amp_ratios)-1:
            plt.xlabel('时间(s)')
    
    plt.suptitle('不同振幅比例对拍频现象的影响')
    plt.tight_layout()
    plt.show()
    
if __name__ == "__main__":
    # 示例调用
    print("=== 任务1: 基本拍频模拟 ===")
    t, wave, beat_freq = simulate_beat_frequency()
    print(f"计算得到的拍频为: {beat_freq} Hz")
    
    print("\n=== 任务2: 参数敏感性分析 ===")
    parameter_sensitivity_analysis()
