import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def one_line_first_method():
    x1 = np.arange(1.0, 10.0, 1.0)
    y1 = 1.6 * x1 + 3.4
    x2 = np.arange(1.0, 10.0, 1.0)
    y2 = 20 * x2**2 + 2 * x2 + 1.8 
    plt.subplot(1, 2, 1)  # 1行2列第1个
    plt.plot(x1, y1)
    plt.xlabel('xlabel')
    plt.ylabel('ylabel')
    plt.title('title')

    plt.subplot(1, 2, 2)  # 1行2列第2个
    plt.plot(x2, y2)
    plt.xlabel('xlabel')

    plt.show()

def one_line_second_method():
    x1 = np.arange(1.0, 10.0, 1.0)
    y1 = 1.6 * x1 + 3.4
    x2 = np.arange(1.0, 10.0, 1.0)
    y2 = 20 * x2**2 + 2 * x2 + 1.8
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)
    ax1.plot(x1, y1)
    ax1.set(xlabel='xlabel', ylabel='ylabel', title='title1')

    ax2.plot(x2, y2)
    ax2.set(xlabel='xlabel', ylabel='ylabel', title='title2')
    plt.show()


if __name__ == "__main__":
    one_line_second_method()