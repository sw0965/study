import numpy as np
from keras.models import Sequential
from keras.layers import Dense, LSTM

#1. 데이터
a = np.array(range(1, 11))
size = 5
print("============453453453================")

print(a)
print("========453243===========")

def split_x(seq, size):    #size = lstm의 timesteps (열)
    aaa = []
    for i in range(len(seq) - size + 1):
        subset = seq[i : (i + size)]
        aaa.append([item for item in subset])   #가장중요
    print(type(aaa))
    return np.array(aaa)

dataset = split_x(a, size)
print("============================")
print(dataset)


'''
def split_x(seq, size):
    aaa = []
    for i in range(len(a) - size + 1):
        subset = a[i : (i + size)]
        print(subset)
        # aaa.append([item for item in subset])
        aaa.append(subset)
    print(type(aaa))
    return np.array(aaa)
    '''