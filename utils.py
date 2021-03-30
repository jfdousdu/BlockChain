import matplotlib
import matplotlib.pyplot as plt



def draw_plt(datas=[], title=None, xlabel='', ylabel='', figsize=(8, 5), mode='show', save_name='', markers= None, colors=None, linestyles = None):
    """绘制图表.
    Args:
        figsize (tuple): 图表大小.
        datas (List[tuple]): 数据元组 (keys, values, label) 的列表.
        title (str): 标题.
        xlabel (str): x轴标题.
        ylabel (str): y轴标题.
        mode (str): 输出模式, show/save.
    """

    if not markers:
        markers = ['o','v','s','^']

    if not colors:
        colors = ['blue', 'green', 'red', 'black', 'purple', 'orange']

    if not linestyles:
        linestyles = ['-', '--', '-.', ':']

    # 初始化图表
    #plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.style.use('default')
    plt.figure(figsize=figsize)
    plt.grid(linestyle="--")  # 设置背景网格线为虚线
    ax = plt.gca()
    ax.spines['top'].set_visible(False)  # 去掉上边框
    ax.spines['right'].set_visible(False)  # 去掉右边框

    # 设置标题 轴名 数据
    if title:
        plt.title(title)
    plt.xticks(fontsize=12, fontweight='bold')  # 默认字体大小为10
    plt.yticks(fontsize=12, fontweight='bold')
    plt.xlabel(xlabel, fontsize=13, fontweight='bold',family = 'SimHei')
    plt.ylabel(ylabel, fontsize=13, fontweight='bold',family = 'SimHei')
    for (keys, values, label), marker, color, linestyle in zip(datas, markers[:len(datas)],colors[:len(datas)],linestyles[:len(datas)]):
        if label:
            plt.plot(list(keys), list(values), label=label, marker = marker, color=color, linestyle = linestyle)
        else:
            plt.plot(list(keys), list(values), marker = marker, color=color, linestyle = linestyle)

            # plt.plot(list(keys), list(values), marker='o', color=color, linestyle = linestyle)

    # 设置图例字体的大小和粗细
    plt.legend()
    leg = plt.gca().get_legend()
    ltext = leg.get_texts()
    plt.setp(ltext, fontsize=12, fontweight='bold',family = 'SimHei')

    # 输出
    if mode == 'show':
        plt.show()
    else:
        plt.savefig(f'./output/{save_name}.svg')  # 和show二选一
        plt.show()


def draw_hist(datas=[], bins=10, title=None, xlabel='', ylabel='', figsize=(8, 5), mode='show', save_name=''):
    """绘制柱状图.
    Args:
        figsize (tuple): 图表大小.
        datas (list): 一维数据列表.
        bins (int): 等距划分长度.
        title (str): 标题.
        xlabel (str): x轴标题.
        ylabel (str): y轴标题.
        mode (str): 输出模式, show/save.
    """
    # 初始化图表
    plt.style.use('default')
    plt.figure(figsize = figsize)
    plt.grid(linestyle="--")  # 设置背景网格线为虚线
    ax = plt.gca()
    ax.spines['top'].set_visible(False)  # 去掉上边框
    ax.spines['right'].set_visible(False)  # 去掉右边框

    # 设置标题 轴名 数据
    if title:
        plt.title(title)
    plt.xticks(fontsize=12, fontweight='bold')  # 默认字体大小为10
    plt.yticks(fontsize=12, fontweight='bold')
    plt.xlabel(xlabel, fontsize=13, fontweight='bold', family = 'SimHei')
    plt.ylabel(ylabel, fontsize=13, fontweight='bold', family = 'SimHei')
    ax.hist(datas, bins=bins)

    # 输出
    if mode == 'show':
        plt.show()
    else:
        plt.show()
        plt.savefig(f'./output/{save_name}.svg')  # 和show二选一

if __name__ == "__main__":
    datas = [
        14, 19, 19, 21, 17, 29, 21, 14, 15, 16, 11, 24, 20, 17, 25, 21, 19, 16, 18, 31, 18, 16, 32, 17, 25, 21, 16, 23,
        19, 19, 17, 19, 22, 20, 17, 13, 13, 20, 21, 16, 15, 16, 18, 18, 22, 18, 22, 18, 16, 23, 18, 26, 24, 26, 19, 27,
        25, 19, 23, 16, 20, 18, 30, 22, 22, 19, 20, 21, 16, 22, 22, 17, 20, 16, 16, 21, 21, 19, 18, 20, 16, 20, 22, 25,
        12, 18, 22, 28, 17, 19, 19, 18, 29, 16, 21, 23, 29, 19, 28, 19
    ]
    draw_hist(datas=datas, bins=20)
