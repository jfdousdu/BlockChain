import numpy as np
import pandas as pd
import time
from collections import Counter


class BlockChain(object):
    '''
    Simulate the blockchain process.

    :param message_pool_size: 最初生成消息队列的长度
    :param n: 系统总结点数
    :param p_n: 系统中参与竞争资源的节点数比例
    :param rd: 迭代轮数，节点请求写区块链次数
    :param strategy: 0(time), 1(gas), 2(50%)
    :param w: 每个参与竞争的节点随机取数的范围[0, w)
    :param p_write_wrong: 计算节点出错概率
    :param p_vote_wrong: 投票节点出错概率
    :param p_success: 写入区块链bound
    :param verbose: True(verbose), False(no verbose)
    :returns: .
    '''
    def __init__(self,
                 message_pool_size,
                 n,
                 p_n,
                 rd,
                 strategy,
                 w,
                 p_write_wrong=0,
                 p_vote_wrong=0,
                 p_success=0.5,
                 verbose=False):
        assert rd <= message_pool_size, 'rd==%d but mps==%d' % (rd, message_pool_size)

        self.n = n
        self.p_n = p_n
        self.rd = rd
        self.strategy = strategy
        self.w = w
        self.p_write_wrong = p_write_wrong
        self.p_vote_wrong = p_vote_wrong
        self.p_success = p_success
        self.verbose = verbose

        # generate message pool randomly
        self.message_pool = np.hstack((
            np.arange(message_pool_size).reshape(-1, 1),  # id
            np.random.randint(int(time.time() - 100000), int(time.time()), message_pool_size).reshape(-1,
                                                                                                      1),  # timestamp
            np.random.randint(1, 1000, message_pool_size).reshape(-1, 1)))  # gas
        if strategy == 0:
            self._sort_pool_by('time')
        elif strategy == 1:
            self._sort_pool_by('gas')

    def get_result(self):
        return self.result

    def print_message_pool(self):
        df = pd.DataFrame(self.message_pool)
        df.columns = ['id', 'timestamp', 'gas']
        print('\n########### Message Pool ###########\n')
        print(df)
        del df

    def start(self):
        '''
        :returns: history
        '''
        self.res_df = pd.DataFrame(columns=['id', 'timestamp', 'gas', 'write_ok', 'vote_ok'])  # 存储每次记录、投票结果
        self._rd = 0
        for i in range(self.rd):
            self._round()
            self._rd += 1

        df = self.res_df
        bc_size = len(df[df['write_ok'] == df['vote_ok']])
        bc_good_size = len(df[(df['write_ok']) & (df['vote_ok'])])
        self.res = {
            'bc_size': bc_size,  # 成功加入blockchain的数量
            'bc_append_prob': bc_size / self.rd,  # 成功加入blockchain的比例
            'bc_good_size': bc_good_size,  # blockchain中好样本数量
            'bc_good_prob': bc_good_size / self.rd,  # 好上链样本的比例
            'bc_good_prob_in_append': bc_good_size / bc_size if bc_size != 0 else 0,  # 上链的blockchain中好样本比例
        }

        if self.verbose:
            print('\n########### Process Table ###########\n')
            print(df)
            print('\n########### Result ###########\n')
            print(self.res)

        del df
        return self.res

    def _round(self):
        """竞争计算机会."""
        # roll = np.random.randint(0, self.w, size=int(round(self.n * self.p_n)))
        # cter = Counter(roll)
        # if 1 not in list(cter.values()):
        #     if self.verbose:
        #         print('Round %d - 竞争失败,本轮轮空.' % self._rd)
        #     return
        #
        # best_w = 0
        # for x, y in zip(cter.keys(), cter.values()):
        #     if y == 1:
        #         best_w = max(best_w, x)
        # cur_node = np.argwhere(roll == best_w).reshape(-1)[0]

        # choose message with strategy
        if self.strategy == 2:
            if np.random.rand() < 0.5:
                self._sort_pool_by('time')
            else:
                self._sort_pool_by('gas')
        msg = self.message_pool[0]

        # write message
        write_ok = np.random.rand() >= self.p_write_wrong  # 记对与否

        # vote
        votes = np.random.rand(self.n - 1)
        votes_prob = len(votes[np.where(votes >= self.p_vote_wrong)]) / len(votes)  # 票对率
        vote_ok = votes_prob >= self.p_success  # 票对与否

        # store or not
        self.res_df = self.res_df.append(pd.Series({
            'id': msg[0],
            'timestamp': msg[1],
            'gas': msg[2],
            'write_ok': write_ok,
            'vote_ok': vote_ok
        }),
                                         ignore_index=True)
        if write_ok == vote_ok:
            self.message_pool = np.delete(self.message_pool, 0, axis=0)

        # log
        # if self.verbose:
        #     print('Round %d - Writer: %d, Id: %d, Gas: %d, Write_OK: %s, Vote_OK: %s, Votes_prob: %.3f' %
        #           (self._rd, cur_node, msg[0], msg[2], write_ok, vote_ok, votes_prob))

    def _sort_pool_by(self, by):
        '''按某列进行排序。
        :param by: 'id', 'time', 'gas'
        '''
        if by == 'id':
            self.message_pool = self.message_pool[self.message_pool[:, 0].argsort()]  # 按第0列排序
        elif by == 'time':
            self.message_pool = self.message_pool[self.message_pool[:, 1].argsort()]  # 按第1列排序
        elif by == 'gas':
            self.message_pool = self.message_pool[self.message_pool[:, 2].argsort()[::-1]]  # 按第2列降序排序


if __name__ == '__main__':
    bc = BlockChain(message_pool_size=100,
                    n=10,
                    p_n=0.3,
                    p_write_wrong=0.2,
                    p_vote_wrong=0.2,
                    p_success=0.75,
                    rd=80,
                    strategy=0,
                    w=5,
                    verbose=True)
    bc.print_message_pool()
    bc.start()
