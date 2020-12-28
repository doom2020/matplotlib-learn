import matplotlib.pyplot as plt



def one_cicle_method():
    labels = ['frogs', 'hogs', 'dogs', 'logs'] # 每一项label
    sizes = [10, 30, 24, 12] # 每一项数值大小
    explode= (0, 0.05, 0.1, 0.2) # 突出显示
    fig, ax = plt.subplots()
    ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)  # autopct 显示输在在每一快上, startangle默认从x正方向切
    ax.axis('equal')
    plt.show()


if __name__ == "__main__":
    one_cicle_method()