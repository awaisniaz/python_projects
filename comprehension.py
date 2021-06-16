import  random
import numpy as np

print(np.arange(1,100,4))
print(np.linspace(1,20,100))
list = [1,2,3,4,5,6,7]
print([i for i in range(len(list)) if i%2 == 0])
from collections import namedtuple,OrderedDict
data2 = {'A':1,'B':4,'R':6}
data2['A'] = 6
print(data2)
data = OrderedDict({'A':1,'B':4,'R':6})
data['B'] = 6
print(data)
print(random.random())
print(random.randint(10,30))
print(random.choice([1,5,7,8,9]))
print(random.shuffle([1,2,6,7,0]))

print(random.random())
random.seed(20)