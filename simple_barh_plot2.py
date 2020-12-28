import matplotlib.pyplot as plt


def one_barh_method():
    labels = ['G1', 'G2', 'G3', 'G4', 'G5']
    men = [30, 22, 18, 50, 60]
    fig, ax = plt.subplots()
    height = 0.5
    ax.barh(labels, men, height)
    ax.set_xlabel('value')
    ax.set_title('title')
    ax.set_ylabel('item')
    ax.grid()
    plt.show()


if __name__ == "__main__":
    one_barh_method()