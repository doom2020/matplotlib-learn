import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import random


def one_scatter_method():
    x_array = np.arange(-1.0, 1.0, 0.01)
    y_array = np.arange(-1.0, 1.0, 0.01)
    random.shuffle(y_array)

    fig, ax = plt.subplots()
    ax.scatter(x_array, y_array)  # 每个点对应坐标的x,y值
    ax.grid()
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('title')
    plt.show()

def two_scatter_method():
    x1_array = np.arange(-1.0, 1.0, 0.01)
    y1_array = np.arange(-1.0, 1.0, 0.01)
    random.shuffle(y1_array)
    x2_array = np.arange(-1.0, 1.0, 0.01)
    y2_array = np.arange(-1.0, 1.0, 0.01)
    random.shuffle(y2_array)

    fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)
    ax1.scatter(x1_array, y1_array)
    ax1.grid()
    ax1.set_ylabel('y1')
    ax1.set_title('title')

    ax2.scatter(x2_array, y2_array)
    ax2.set_ylabel('y2')
    ax2.set_xlabel('x')

    plt.show()


def two_scatter_method_two():
    x1_array = np.arange(-1.0, 1.0, 0.01)
    y1_array = np.arange(-1.0, 1.0, 0.01)
    random.shuffle(y1_array)
    x2_array = np.arange(-1.0, 1.0, 0.01)
    y2_array = np.arange(-1.0, 1.0, 0.01)
    random.shuffle(y2_array)
    plt.subplot(2, 1, 1)
    plt.scatter(x1_array, y1_array)
    plt.title('1')
    plt.ylabel('y1')
    plt.grid()
    plt.subplot(2, 1, 2)
    plt.scatter(x2_array, y2_array)
    plt.grid()
    plt.xlabel('x')
    plt.ylabel('y2')
    plt.show()


if __name__ == "__main__":
    two_scatter_method_two()
