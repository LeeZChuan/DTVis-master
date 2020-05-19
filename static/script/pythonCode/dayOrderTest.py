# -*- coding: utf-8 -*-
"""

@author: LeeZChuan


"""

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import torch 
from torch import nn
from torch.autograd import Variable
 
 
 
filename = 'dayOrderRaw.csv' 
data_df = pd.read_csv(filename, engine='python', encoding='utf_8_sig').loc[:,['date','order']]

print (data_df.shape)

data_csv = [item for item in data_df['order'] if int(item) > 1000]

data_csv = pd.DataFrame(data_csv)

print (data_csv.shape)


data_date = [item for item in data_df['order'] if int(item) > 1000]
 
# plt.plot(data_csv)
# plt.show()
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
        dataX.append(a)#步长为2的预测算法训练集
        dataY.append(dataset[i+look_back])
    return np.array(dataX), np.array(dataY)
 
data_X, data_Y = create_dataset(dataset)
 
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
        super(lstm_reg,self).__init__()#input_size：x的特征维度
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
 
 
net = lstm_reg(2,4)
 
net.load_state_dict(torch.load('net_params.pkl')) 
 
data_X = data_X.reshape(-1, 1, 2)
data_X = torch.from_numpy(data_X)
var_data = Variable(data_X)
pred_test = net(var_data) # 测试集的预测结果
pred_test = pred_test.view(-1).data.numpy()
 
plt.plot(pred_test, 'r', label='prediction')
plt.plot(dataset, 'b', label='real')
plt.legend(loc='best')
plt.show()


pre = pred_test
pre = [item*scalar for item in pre]
print (pre)


fileSave = 'dayOrder.csv'  
    
df = pd.DataFrame(pre, columns=['prediction']) 

df.to_csv(fileSave, encoding='utf_8_sig')

