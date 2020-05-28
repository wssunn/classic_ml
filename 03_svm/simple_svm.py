import numpy as np

if __name__ == "__main__":
    X = np.array([[-3, 1], [-2, 1], [-1, 1], [1, 1], [2, -1], [3, -1]])
    y = np.array([-1, -1, -1, 1, 1, 1])
    svm_model = SVM(X, y)
    svm_model.train()
    w, b = svm_model.model()
    print('w=', w, 'b= ', b)


class SVM:
    def __init__(self, x_data, y_data, epsilon=0.001, c=None, algo='smo'):
        self._x_data = x_data
        self._y_data = y_data
        self._a = np.array([1.]*len(self.x_data)) #float
        self._b = 0.0 #待求变量
        self._w = None #待求变量
        self._K = self._cal_kernel() #xi^T xj, array
        self._E = self._cal_E() # Ei = f(xi)-yi, list
        self._epsilon = epsilon #精度误差
        self._c = c #soft margin
        self._algo = algo
    
    # 对外接口
    def train(self):
        pass

    def model(self):
        pass

    def _smo(self):
        counter = 100
        while 1:
            id_a1, id_a2 = self._choose_a()
            self._update(id_a1, id_a2)
            if self._satisfy() or counter == 0:
                break
            counter -= 1

    def _choose_a(self):
        a1_id, a2_id = None, None
        on_bound_id = [] # svm id
        remain_id = []   # non_svm id
        # 筛选出 支持向量 和 非支持向量
        for i in range(len(self._a)):
            if self._a[i] > 0 and (self._c is None or self._a[i] < self._c):
                on_bound_id.append(i)
            else:
                remain_id.append(i)
        
        # 正式开始找 a1, a2
        for i in on_bound_id:
            # 找不满足KKT条件的伪 支持向量，为a1
            if not (1-self._epsilon <= self._y_data[i] * self._g(i) <= 1+self._epsilon):
                a2_id = self._choose_a2(i, on_bound_id, remain_id)
                if a2_id is not None:
                    a1_id = i
                    return a1_id, a2_id

        # 如果所有 支持向量 都找遍了，就只能找其他数据点作为a1
        for i in remain_id:
            if self._a[i] == 0:
                if not (1-self._epsilon <= self._y_data[i]*self._g(i)):
                    pass

 
    def _choose_a2(self, a1_id, on_bound_id, remain_id):
        pass

    def _satisfy(self):
        pass

    def _update(self, id1, id2):
        pass

    def _check_enough_diff(self, id1, id2):
        pass

    def clip_a2(self, a2, id1, id2):
        pass

    def _g(self, index):
        pass

    def _cal_kernel(self):
        pass
