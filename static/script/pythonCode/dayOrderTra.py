# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 13:54:56 2019

@author: Administrator
"""


import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import torch 
from torch import nn
from torch.autograd import Variable
 
 #数据读取
filename = 'dayOrder.csv' 
data_df = pd.read_csv(filename, engine='python', encoding='utf_8_sig').loc[:,['order']]
data_csv = [item for item in data_df['order'] if int(item) > 1000]
data_csv = pd.DataFrame(data_csv)

#数据预处理
data_csv = data_csv.dropna() #去掉na数据
dataset = data_csv.values
dataset = dataset.astype('float32')
max_value = np.max(dataset)
min_value = np.min(dataset)
scalar = max_value-min_value
dataset = list(map(lambda x: x/scalar, dataset)) #将数据标准化到0~1之间
 
def create_dataset(dataset,look_back=2):
    dataX, dataY=[], []
    for i in range(len(dataset)-look_back):
        a=dataset[i:(i+look_back)]
        dataX.append(a)
        dataY.append(dataset[i+look_back])
    return np.array(dataX), np.array(dataY)
 
data_X, data_Y = create_dataset(dataset)
print (len(data_X[0]), len(data_Y[0]))
 
#划分训练集和测试集，70%作为训练集
train_size = int(len(data_X) * 0.7)
test_size = len(data_X)-train_size
 
train_X = data_X[:train_size]
train_Y = data_Y[:train_size]
 
test_X = data_X[train_size:]
test_Y = data_Y[train_size:]
 
train_X = train_X.reshape(-1,1,2)
train_Y = train_Y.reshape(-1,1,1)

test_X = test_X.reshape(-1,1,2)
train_x = torch.from_numpy(train_X)
train_y = torch.from_numpy(train_Y)
test_x = torch.from_numpy(test_X)
 
class lstm_reg(nn.Module):
    def __init__(self,input_size,hidden_size, output_size=1,num_layers=2):
        super(lstm_reg,self).__init__()#super() 函数是用于调用父类(超类)的一个方法。
        #input_size：x的特征维度
        #num_layers：lstm隐层的层数，默认为1
        #hidden_size：隐藏层的特征维度
 
        self.rnn = nn.LSTM(input_size,hidden_size,num_layers)
        self.reg = nn.Linear(hidden_size,output_size)
 
    def forward(self,x):
        x, _ = self.rnn(x)
        s,b,h = x.shape
        x = x.view(s*b, h)
        x = self.reg(x)
        x = x.view(s,b,-1)
        return x
        
#LSTM层数为2，隐藏层大小为4。
net = lstm_reg(2,4)
criterion = nn.MSELoss()#均方误差损失MSELoss（），预测出来的值与
optimizer = torch.optim.Adam(net.parameters(),lr=1e-2)#优化程序
#lr为学习率
#net.parameters()构建好神经网络后，网络的参数都保存再paeameters函数里面 
for e in range(5000):
    var_x = Variable(train_x)
    var_y = Variable(train_y)
 
    out = net(var_x)
    loss = criterion(out, var_y)
 
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    if (e+1)%100 == 0:
    #整数循环输出目前的丢失率以及其他相关信息
        print('Epoch: {}, Loss:{:.5f}'.format(e+1, loss.data[0]))
        
torch.save(net.state_dict(), 'net_params.pkl')
