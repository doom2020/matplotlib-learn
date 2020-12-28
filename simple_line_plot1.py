import matplotlib
import matplotlib.pyplot as plt
import numpy as np



def methods_one():
    x = np.arange(0.0, 2.0, 0.01)
    y = 1 + np.sin(2 * np.pi * x)


    fig, ax = plt.subplots(nrows=1, ncols=1)  # 适合创建多个子图一个fig里面可以有多个ax(子图) 几行几列 fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3)
    plt.subplot()
    ax.plot(x, y)

    ax.set(xlabel='x', ylabel='y', title='xy img')

    ax.grid()

    plt.show()

def methods_two():
    x = np.arange(0.0, 2.0, 0.01)
    y = 1 + np.sin(2 * np.pi * x)
    plt.subplot(1, 1, 1)  # 适合创建一个子图可简写plt.subplot() 表示第一行第一列的第一个
    plt.plot(x, y, 'o-')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('x-y img')
    plt.grid()
    plt.show()

if __name__ == "__main__":
    methods_two()
