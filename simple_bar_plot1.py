import matplotlib.pyplot as plt



def one_bar_method():
    labels = ['G1', 'G2', 'G3', 'G4', 'G5']  # 相当于x坐标
    men = [20, 35, 30, 35, 27] # 相当于y坐标
    width = 0.35 # 条形图的宽度
    fig, ax = plt.subplots()
    ax.bar(labels, men, width, label='men') # 显示legend
    ax.set_ylabel('score')
    ax.set_title('title')
    ax.legend()
    plt.show()


def two_bar_method():
    labels = ['G1', 'G2', 'G3', 'G4', 'G5']
    men = [20, 35, 30, 35, 27]
    women = [20, 35, 30, 35, 27]
    width = 0.5
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.bar(labels, men, width)
    ax1.set_ylabel('score')
    ax1.set_title('title')

    ax2.bar(labels, women, width)
    ax2.set_ylabel('score2')
    ax2.set_title('title2')
    plt.show()


if __name__ == "__main__":
    two_bar_method()