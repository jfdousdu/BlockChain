import numpy as np
from block_chain import BlockChain
from utils import draw_plt


def draw_extra3_1():
    """写链错误率对好写链比例的影响."""
    MESSAGE_POOL_SIZE = 100
    NODES = 30
    ROUND = 50
    P_N = 0.1
    STRATEGY = 1
    W = 5
    P_WRITE_WRONG = np.arange(0.1, 0.5001, 0.05)
    P_VOTE_WRONG = [0.2, 0.3, 0.4, 0.5]

    res = {rate: dict() for rate in P_VOTE_WRONG}

    for pvw in P_VOTE_WRONG:
        print(f'P_VOTE_WRONG rate {pvw}')
        for pww in P_WRITE_WRONG:
            tmp = []
            for _ in range(5):
                bc = BlockChain(message_pool_size=MESSAGE_POOL_SIZE,
                                n=NODES,
                                p_n=P_N,
                                rd=ROUND,
                                strategy=STRATEGY,
                                w=W,
                                p_write_wrong=pww,
                                p_vote_wrong=pvw,
                                verbose=False)
                write_stat = bc.start()
                tmp.append(write_stat['bc_good_prob_in_append'])
            res[pvw][pww] = np.mean(tmp)

    # 绘制结果曲线
    draw_plt(datas=[(res[k].keys(), res[k].values(), f'投票错误的概率={k}') for k in P_VOTE_WRONG],
             xlabel='领导节点发布错误区块的概率',
             ylabel='正确区块所占比例',
             mode='save',
             save_name='Block Chain pww & writerate')


def draw_extra3_2():
    """投票错误率对好写链比例的影响."""
    MESSAGE_POOL_SIZE = 100
    NODES = 30
    ROUND = 50
    P_N = 0.1
    STRATEGY = 1
    W = 5
    P_WRITE_WRONG = [0.1, 0.3, 0.5]
    P_VOTE_WRONG = np.arange(0.1, 0.5001, 0.05)

    res = {rate: dict() for rate in P_WRITE_WRONG}

    for pww in P_WRITE_WRONG:
        print(f'P_WRITE_WRONG rate {pww}')
        for pvw in P_VOTE_WRONG:
            tmp = []
            for _ in range(5):
                bc = BlockChain(message_pool_size=MESSAGE_POOL_SIZE,
                                n=NODES,
                                p_n=P_N,
                                rd=ROUND,
                                strategy=STRATEGY,
                                w=W,
                                p_write_wrong=pww,
                                p_vote_wrong=pvw,
                                verbose=False)
                write_stat = bc.start()
                tmp.append(write_stat['bc_good_prob_in_append'])
            res[pww][pvw] = np.mean(tmp)

    # 绘制结果曲线
    draw_plt(datas=[(res[k].keys(), res[k].values(), f'领导节点发布错误区块的概率={k}') for k in P_WRITE_WRONG],
             xlabel='投票错误的概率',
             ylabel='正确区块所占比例',
             mode='save',
             save_name='Block Chain pvw & writerate')


if __name__ == "__main__":
    draw_extra3_1()
    draw_extra3_2()
