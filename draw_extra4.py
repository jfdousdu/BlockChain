import numpy as np
from utils import draw_plt


def draw_extra4():
    n = np.arange(10, 60, 10)
    datas = [(n, 2 * n**2 - n - 1, 'kPBFT'), (n, n**2 + n * 3-2, '本协议')]

    draw_plt(datas=datas, xlabel='共识节点的数量', ylabel='通信量', mode='save', save_name='node & communication')


if __name__ == "__main__":
    draw_extra4()
