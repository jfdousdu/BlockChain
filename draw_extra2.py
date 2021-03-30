import numpy as np
from utils import draw_hist


def draw_extra2():
    """共识节点转leader次数正态分布."""
    ROUND = 10000  # 共识轮数
    RATE_F2C = 0.2  # 全节点2共识节点概率
    POINT_AMOUNT = 500  # 全节点个数

    leader_count = [0 for _ in range(POINT_AMOUNT)]

    for i in range(ROUND):
        c_indexes = np.where(np.random.rand(POINT_AMOUNT) < RATE_F2C)[0]  # 成为共识节点的编号
        if len(c_indexes) > 0:
            leader = np.random.choice(c_indexes)
            leader_count[leader] += 1
    # print(leader_count)
    draw_hist(datas=leader_count,
              bins=12,
              xlabel='全节点成为领导节点的频率',
              ylabel='全节点的数量',
              mode='save',
              save_name='C2l dist')


if __name__ == "__main__":
    draw_extra2()
