import numpy as np
from block_chain import BlockChain
from utils import draw_plt



def draw1():
    params = {
        'message_pool_size': 10000,
        'n': 30,
        'rd': [2000, 5000, 10000],
        'p_n': np.arange(0.1, 1.01, 0.1),
        'strategy': 1,
        'w': 5,
    }
    res = dict()
    for rd in params['rd']:
        res[rd] = dict()

    for rd in params['rd']:
        print('rd %d' % rd)
        for p_n in params['p_n']:
            p_n = round(p_n, 2)
            tmp = []
            for _ in range(5):
                bc = BlockChain(message_pool_size=params['message_pool_size'],
                                n=params['n'],
                                p_n=p_n,
                                rd=rd,
                                strategy=params['strategy'],
                                w=params['w'],
                                verbose=False)
                tmp.append(bc.start()['bc_size'])
            res[rd][p_n] = np.mean(tmp)/(3*params['n']*p_n - 2)

    # 绘制结果曲线
    draw_plt(datas=[(res[k].keys(), res[k].values(), f'通信量={k}') for k in [2000, 5000, 10000]],
             xlabel='全节点的活跃度',
             ylabel='领导节点产生的轮数',
             mode='save',
             save_name='Block Chain p_n & Leader Node Counts n=30')


# def draw2():
#     params = {
#         'message_pool_size': 1000,
#         'n': 30,
#         'rd': [20, 50, 100],
#         'p_n': 0.5,
#         'strategy': 1,
#         'w': np.arange(2, 10),
#     }
#     res = dict()
#     for rd in params['rd']:
#         res[rd] = dict()
#
#     for rd in params['rd']:
#         print('rd %d' % rd)
#         for w in params['w']:
#             tmp = []
#             for _ in range(5):
#                 bc = BlockChain(message_pool_size=params['message_pool_size'],
#                                 n=params['n'],
#                                 p_n=params['p_n'],
#                                 rd=rd,
#                                 strategy=params['strategy'],
#                                 w=w,
#                                 verbose=False)
#                 tmp.append(bc.start()['bc_size'])
#             res[rd][w] = np.mean(tmp)
#
#     # 绘制结果曲线
#     draw_plt(datas=[(res[k].keys(), res[k].values(), f'Round={k}') for k in [20, 50, 100]],
#              xlabel='Intensity of Competition',
#              ylabel='Number of Nodes',
#              mode='show',
#              save_name='Block Chain w & bc_size')


def draw3():
    params = {
        'message_pool_size': 10000,
        'n': 60,
        'rd': [2000, 5000, 10000],
        'p_n': np.arange(0.1, 1.01, 0.1),
        'strategy': 1,
        'w': 5,
    }
    res = dict()
    for rd in params['rd']:
        res[rd] = dict()

    for rd in params['rd']:
        print('rd %d' % rd)
        for p_n in params['p_n']:
            p_n = round(p_n, 2)
            tmp = []
            for _ in range(5):
                bc = BlockChain(message_pool_size=params['message_pool_size'],
                                n=params['n'],
                                p_n=p_n,
                                rd=rd,
                                strategy=params['strategy'],
                                w=params['w'],
                                verbose=False)
                tmp.append(bc.start()['bc_size'])
            res[rd][p_n] = np.mean(tmp)/(3*params['n']*p_n - 2)

    # 绘制结果曲线
    draw_plt(datas=[(res[k].keys(), res[k].values(), f'通信量={k}') for k in [2000, 5000, 10000]],
             xlabel='全节点的活跃度',
             ylabel='领导节点产生的轮数',
             mode='save',
             save_name='Block Chain p_n & Leader Node Counts n=60')


# def draw4():
#     params = {
#         'message_pool_size': 10000,
#         'n': 30,
#         'rd': [2000, 5000, 10000],
#         'p_n': np.arange(0.1, 1.01, 0.1),
#         'strategy': 1,
#         'w': 5,
#     }
#     res = dict()
#     for rd in params['rd']:
#         res[rd] = dict()
#
#     for rd in params['rd']:
#         print('rd %d' % rd)
#         for p_n in params['p_n']:
#             p_n = round(p_n, 2)
#             tmp = []
#             for _ in range(5):
#                 bc = BlockChain(message_pool_size=params['message_pool_size'],
#                                 n=params['n'],
#                                 p_n=p_n,
#                                 rd=rd,
#                                 strategy=params['strategy'],
#                                 w=params['w'],
#                                 verbose=False)
#                 tmp.append(bc.start()['bc_size'])
#             res[rd][p_n] = np.mean(tmp)/(params['n']*params['n'])
#
#     # 绘制结果曲线
#     draw_plt(datas=[(res[k].keys(), res[k].values(), f'通信量={k}') for k in [2000, 5000, 10000]],
#              xlabel='全节点的活跃度',
#              ylabel='共识阶段的轮数',
#              mode='save',
#              save_name='Block Chain p_n & Consenus Counts n=30')
#
# def draw5():
#     params = {
#         'message_pool_size': 10000,
#         'n': 60,
#         'rd': [2000, 5000, 10000],
#         'p_n': np.arange(0.1, 1.01, 0.1),
#         'strategy': 1,
#         'w': 5,
#     }
#     res = dict()
#     for rd in params['rd']:
#         res[rd] = dict()
#
#     for rd in params['rd']:
#         print('rd %d' % rd)
#         for p_n in params['p_n']:
#             p_n = round(p_n, 2)
#             tmp = []
#             for _ in range(5):
#                 bc = BlockChain(message_pool_size=params['message_pool_size'],
#                                 n=params['n'],
#                                 p_n=p_n,
#                                 rd=rd,
#                                 strategy=params['strategy'],
#                                 w=params['w'],
#                                 verbose=False)
#                 tmp.append(bc.start()['bc_size'])
#             res[rd][p_n] = np.mean(tmp)/(params['n']*params['n'])
#
#     # 绘制结果曲线
#     draw_plt(datas=[(res[k].keys(), res[k].values(), f'通信量={k}') for k in [2000, 5000, 10000]],
#              xlabel='全节点的活跃度',
#              ylabel='共识阶段的轮数',
#              mode='save',
#              save_name='Block Chain p_n & Consensus Counts n=60')
#
# def draw6():
#     params = {
#         'message_pool_size': 10000,
#         'n': 30,
#         'rd': [2000, 5000, 10000],
#         'p_n': np.arange(0.1, 1.01, 0.1),
#         'strategy': 1,
#         'w': 5,
#     }
#     res = dict()
#     for rd in params['rd']:
#         res[rd] = dict()
#
#     for rd in params['rd']:
#         print('rd %d' % rd)
#         for p_n in params['p_n']:
#             p_n = round(p_n, 2)
#             tmp = []
#             for _ in range(5):
#                 bc = BlockChain(message_pool_size=params['message_pool_size'],
#                                 n=params['n'],
#                                 p_n=p_n,
#                                 rd=rd,
#                                 strategy=params['strategy'],
#                                 w=params['w'],
#                                 verbose=False)
#                 tmp.append(bc.start()['bc_size'])
#             res[rd][p_n] = np.mean(tmp)/(3*params['n']*p_n - 2 + params['n']*params['n'])
#
#     # 绘制结果曲线
#     draw_plt(datas=[(res[k].keys(), res[k].values(), f'通信量={k}') for k in [2000, 5000, 10000]],
#              xlabel='全节点的活跃度',
#              ylabel='协议的轮数',
#              mode='save',
#              save_name='Block Chain p_n & SM Counts n=30')
#
# def draw7():
#     params = {
#         'message_pool_size': 10000,
#         'n': 60,
#         'rd': [2000, 5000, 10000],
#         'p_n': np.arange(0.1, 1.01, 0.1),
#         'strategy': 1,
#         'w': 5,
#     }
#     res = dict()
#     for rd in params['rd']:
#         res[rd] = dict()
#
#     for rd in params['rd']:
#         print('rd %d' % rd)
#         for p_n in params['p_n']:
#             p_n = round(p_n, 2)
#             tmp = []
#             for _ in range(5):
#                 bc = BlockChain(message_pool_size=params['message_pool_size'],
#                                 n=params['n'],
#                                 p_n=p_n,
#                                 rd=rd,
#                                 strategy=params['strategy'],
#                                 w=params['w'],
#                                 verbose=False)
#                 tmp.append(bc.start()['bc_size'])
#             res[rd][p_n] = np.mean(tmp)/(3*params['n']*p_n - 2 + params['n']*params['n'])
#
#     # 绘制结果曲线
#     draw_plt(datas=[(res[k].keys(), res[k].values(), f'通信量={k}') for k in [2000, 5000, 10000]],
#              xlabel='全节点的活跃度',
#              ylabel='协议的轮数',
#              mode='save',
#              save_name='Block Chain p_n & SM Counts n=60')

if __name__ == "__main__":
    draw1()
    # draw2()
    draw3()

    # draw4()
    # draw5()
    #
    # draw6()
    # draw7()