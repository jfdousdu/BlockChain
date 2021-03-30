import numpy as np
from block_chain import BlockChain
from utils import draw_plt


def draw_extra1_1():
    """全节点转共识节点概率对上链比例的影响."""
    MESSAGE_POOL_SIZE = 1000
    NODES = 30
    ROUND = [20, 50, 100]
    P_N = np.arange(0.1, 1.01, 0.1)
    STRATEGY = 1
    W = 5
    P_WRITE_WRONG = 0.2
    P_VOTE_WRONG = 0.2

    res = {rd: dict() for rd in ROUND}

    for rd in ROUND:
        print(f'Round {rd}')
        for pn in P_N:
            tmp = []
            for _ in range(5):
                bc = BlockChain(message_pool_size=MESSAGE_POOL_SIZE,
                                n=NODES,
                                p_n=pn,
                                rd=rd,
                                strategy=STRATEGY,
                                w=W,
                                p_write_wrong=P_WRITE_WRONG,
                                p_vote_wrong=P_VOTE_WRONG,
                                verbose=False)
                write_stat = bc.start()
                tmp.append(write_stat['bc_good_prob'])
            res[rd][pn] = np.mean(tmp)

    # 绘制结果曲线
    draw_plt(datas=[(res[k].keys(), res[k].values(), f' ={k}') for k in ROUND],
             xlabel='Probability of Consensus Nodes from Full Nodes',
             ylabel='Good Write Probability',
             mode='show',
             save_name='Block Chain p_n & goodwriterate & round')


def draw_extra1_2():
    """全节点转共识节点概率对上链比例的影响."""
    MESSAGE_POOL_SIZE = 100
    NODES = [10, 30, 50]
    ROUND = 20
    P_N = np.arange(0.1, 1.01, 0.1)
    STRATEGY = 1
    W = 5
    P_WRITE_WRONG = 0.2
    P_VOTE_WRONG = 0.2

    res = {n: dict() for n in NODES}

    for n in NODES:
        print(f'Nodes {n}')
        for pn in P_N:
            tmp = []
            for _ in range(5):
                bc = BlockChain(message_pool_size=MESSAGE_POOL_SIZE,
                                n=n,
                                p_n=pn,
                                rd=ROUND,
                                strategy=STRATEGY,
                                w=W,
                                p_write_wrong=P_WRITE_WRONG,
                                p_vote_wrong=P_VOTE_WRONG,
                                verbose=False)
                write_stat = bc.start()
                tmp.append(write_stat['bc_good_prob'])
            res[n][pn] = np.mean(tmp)

    # 绘制结果曲线
    draw_plt(datas=[(res[k].keys(), res[k].values(), f'Nodes={k}') for k in NODES],
             xlabel='Probability of Consensus Nodes from Full Nodes',
             ylabel='Good Write Probability',
             mode='show',
             save_name='Block Chain p_n & goodwriterate & nodes')


if __name__ == "__main__":
    draw_extra1_1()
    draw_extra1_2()
