import torch as t
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

t.manual_seed(100)
dtype = t.float

x = t.unsqueeze(t.linspace(-1, 1, 100), dim = 1)
y = 3 * x.pow(2) + 2 + 0.2 * t.rand(x.size())

plt.scatter()
plt.show()

w = t.randn(1, 1, dtype=dtype, requires_grad=True)
b = t.zeros(1, 1, dtype=dtype, requires_grad=True)

lr = 0.001
