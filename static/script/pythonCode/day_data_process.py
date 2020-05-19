# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 14:59:51 2019

@author: chris
"""

import pandas as pd
import numpy as np
import requests
import os
from pandas.core.frame import DataFrame
import json
import datetime
import time

pd.set_option('display.max_columns',1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth',1000)




def addressProcess(address):
    result = address
    
    if '镇' in address:
        item = address.split('镇')
        result = item[0]+'镇'
    elif '农场' in address:
        item = address.split('农场')
        result = item[0]+'农场'
    elif '街道' in address:
        item = address.split('街道')
        result = item[0]+'街道'
    elif '路' in address:
        item = address.split('路')
        result = item[0]+'路'
    elif '大道' in address:
        item = address.split('大道')
        result = item[0]+'大道'
    elif '街' in address:
        item = address.split('街')
        result = item[0]+'街'
    elif '村' in address:
        item = address.split('村')
        result = item[0]+'村'
    return result

def processJson(filePath):
    
    orderNum = 0  #订单数
    
    with open(filepath, 'r', encoding="utf-8") as f:
            # 读取所有行 每行会是一个字符串  
            i = 0
            for jsonstr in f.readlines():
                
                list_address = []
                
                list_name = []
                
                jsonstr = jsonstr[1:-1]
#                listValue = jsonstr.split(']];,')
                listValue = jsonstr.split(']],')
    

                for listitem in listValue:
                    listitem = listitem[1:]
                    
                    listCon = listitem.split(',[')

                    
                    listAddr = listCon[3][:-1].split(',')

                    if len(listAddr) == 2 and '海南省海口市' in listAddr[0] and '海南省海口市' in listAddr[1]:
                        
                        list_address_each = []
                        
                        startAdd = addressProcess(listAddr[0][6:])
                        endAdd = addressProcess(listAddr[1][6:])
                        
                        if startAdd != endAdd:
                            
                            list_address_each.append(startAdd)
                            list_address_each.append(endAdd)
                            list_address.append(list_address_each)
                            
                            list_name.append(startAdd)
                            list_name.append(endAdd)
                               
            pd_list_address = pd.DataFrame(list_name)
#            print (pd_list_address)
            name_list_count = pd.value_counts(pd_list_address[0], sort=False)
            name_df = pd_list_address[0].unique()
            name_list = name_df.tolist()
            

            name_list_all = [[name, name_list_count[name]] for name in name_list if name_list_count[name] > 300]

            
            name_list_new = []
            for item in name_list_all:
                name_list_new.append(item[0])
                
            print (name_list_new)
            new_list_address = []
            for item in list_address:
                if item[0] in name_list_new and item[1] in name_list_new:
                    new_list = []
                    new_list.append(item[0])
                    new_list.append(item[1])
                    new_list_address.append(new_list)
                    orderNum += 1
             
    return orderNum, list_address



def save(filename, contents):
    fh = open(filename, 'w', encoding='utf-8')
    fh.write(contents)
    fh.close()

def dataSta(list_address, txtname):
    
    raw_file_df = pd.DataFrame(list_address)

    
    raw_file_df.dropna(axis=0, how='any', inplace=True) #删除含有空值的行
    result = raw_file_df.groupby([raw_file_df[0],raw_file_df[1]])
    
    all_result = []
    name_result = []
    for name, item in result:
        each_result = []
        each_result.append(name[0])
        each_result.append(name[1])
        each_result.append(len(item))
        all_result.append(each_result)
        
        name_result.append(name[0])
        name_result.append(name[1])
        
    name_df = DataFrame(name_result)
    name_list_count = pd.value_counts(name_df[0], sort=False)
    name_df = name_df[0].unique()
    name_list = name_df.tolist()
    
    name_list_all = [[name, name_list_count[name]] for name in name_list]
    
    print (name_list_all)
    

    strValue = "{\"nodes\": [\n"
    for item in name_list_all:
        strValue = strValue+"    {\"name\":\""+item[0] +"\",\n    \"value\":"+str(item[1])+"    \n    },\n"
    strValue = strValue[:-2]
    strValue = strValue + "\n    ],\n"
        
    strValue = strValue + "\"links\": [\n"
    for item in all_result:
        strValue = strValue+"    {\"source\":\""+item[0]+"\", \"target\":\""+item[1]+"\", \"value\":"+str(item[2])+"\n    },\n"
    
    strValue = strValue[:-2]
    strValue = strValue + "\n    ]\n}"

    name_path = os.getcwd()+'\dataForMulberryFigure\\'+txtname+'_nodes_links.json'

    

    save(name_path, strValue)
    
    

def hexiantu(list_address, txtname):
    
    raw_file_df = pd.DataFrame(list_address)

    
    raw_file_df.dropna(axis=0, how='any', inplace=True) #删除含有空值的行
    result = raw_file_df.groupby([raw_file_df[0],raw_file_df[1]])
    
    all_result = []
    for name, item in result:
        each_result = []
        each_result.append(name[0])
        each_result.append(name[1])
        each_result.append(len(item))
        all_result.append(each_result)
        
    strValue = ''    
    strValue = strValue + "{\"value\": [\n"
    for item in all_result:
        strValue = strValue+"    [\""+item[0]+"\", \""+item[1]+"\", "+str(item[2])+"],\n"
    
    strValue = strValue[:-2]
    strValue = strValue + "\n    ]}"
    name_path = os.getcwd()+'\dataForMulberryFigure\\'+txtname+'_hexiantu.json'
    save(name_path, strValue)





def read_csv(filepath):
#    raw_train_df = pd.read_csv(fileInfo, sep='\s+', engine='python').loc[:,[name_title+'arrive_time',name_title+'starting_lng',name_title+'starting_lat',name_title+'dest_lng',name_title+'dest_lat']]
    raw_train_df = pd.read_csv(filepath, sep=',', engine='python').loc[:,['order_id','product_id','type','combo_type','traffic_type','passenger_count', 'driver_product_id', 'start_dest_distance', 'arrive_time', 'departure_time', 'pre_total_fee', 'normal_time', 'bubble_trace_id', 'product_1level', 'year', 'month', 'year', 'starting_lng', 'starting_lat', 'dest_lng', 'dest_lat']]
    return raw_train_df


def orderNumByHour(filepath, txtname):
    raw_train_df = read_csv(filepath)    
    raw_train_df['hour'] = [pd.to_datetime(item).hour for item in raw_train_df['departure_time']]
    result = ''
    result_distance = '[\n'
    groupedByHour = raw_train_df.groupby(['hour'])
    for group_name, group_data in groupedByHour:
        result = result+str(group_name)+','+str(group_data.shape[0])+'\n'
        result_distance = result_distance +'    [\n        \"'+str(group_name)+'\",\n        '+str(group_data.shape[0])+',\n        '+str(int(group_data['passenger_count'].mean())/1000)+'\n    ],\n'
    result_order = result_distance[:-2] + '\n]'  
    name_path = os.getcwd()+'\lineChart\\'+txtname+'_lineChart.json'
    save(name_path, result_order)


def save2(filepath, filename, contents):
    if not os.path.exists(filepath):
        os.mkdir(filepath)
    path = filepath + '\\' + filename
    fh = open(path, 'w', encoding='utf-8')
    fh.write(contents)
    fh.close()        


def averagenum(num):
    nsum = 0
    for i in range(len(num)):
        nsum += num[i]
    return nsum / len(num)


def grade_mode(list):
    '''
    计算众数
    参数：
        list：列表类型，待分析数据    
    返回值：
        grade_mode: 列表类型，待分析数据的众数     
    '''
    # TODO
    # 定义计算众数的函数
    # grade_mode返回为一个列表，可记录一个或者多个众数
 
    list_set=set(list)#取list的集合，去除重复元素
    frequency_dict={}
    for i in list_set:#遍历每一个list的元素，得到该元素何其对应的个数.count(i)
        frequency_dict[i]=list.count(i)#创建dict; new_dict[key]=value
    grade_mode=[]
    for key,value in frequency_dict.items():#遍历dict的key and value。key:value
        if value==max(frequency_dict.values()):
            grade_mode.append(key)






def thermodynamicByHour(filepath, txtname):
    raw_train_df = read_csv(filepath)    
    raw_train_df['hour'] = [pd.to_datetime(item).hour for item in raw_train_df['departure_time']]
    list_count_start = []
    list_count_end = []
    
    groupedByHour = raw_train_df.groupby(['hour'])
    for group_name, group_data in groupedByHour:
        print ('处理数据的时间段：', group_name)
        result = '[\n'
        groupByLocation = group_data.groupby([group_data['starting_lng'],group_data['starting_lat']])
        for group_name2, group_data2 in groupByLocation:
            list_count_start.append(len(group_data2))
            if group_name2[0] > 100 and group_name2[1] < 40:
                result = result + '    {\n        \"lng\": ' + str(group_name2[0]) + ',\n        \"lat\": ' + str(group_name2[1]) + ',\n        \"count\": ' + str(len(group_data2)) + '\n    },\n'
        result = result[:-2] + '\n]'
            
        result2 = '[\n'
        groupByLocation2 = group_data.groupby([group_data['dest_lng'],group_data['dest_lat']])
        for group_name3, group_data3 in groupByLocation2:
            list_count_end.append(len(group_data3))
            if group_name3[0] > 100 and group_name3[1] < 40:
                result2 = result2 + '    {\n        \"lng\": ' + str(group_name3[0]) + ',\n        \"lat\": ' + str(group_name3[1]) + ',\n        \"count\": ' + str(len(group_data3)) + '\n    },\n'
        result2 = result2[:-2] + '\n]'
            
        
        txt_start = txtname+'_start'
        txt_dest = txtname+'_dest'
        path_start = os.getcwd()+'\dataForMulberryFigure\\'+txt_start
        path_dest = os.getcwd()+'\dataForMulberryFigure\\'+txt_dest
        name = str(group_name)+'.json'
        save2(path_start, name, result)   
        save2(path_dest, name, result2)



def get_week_day(date):
  week_day_dict = {
    0 : '星期一',
    1 : '星期二',
    2 : '星期三',
    3 : '星期四',
    4 : '星期五',
    5 : '星期六',
    6 : '星期天',
  }
  day = date.weekday()
  return week_day_dict[day]


def strGetAve(str1, str2):
    return ((int(str1)+int(str2))/2)

def calendarHeatMap(foldername):
    
    weatherPath = 'weather_05.xlsx'
    weather_df = pd.DataFrame(pd.read_excel(weatherPath))
    weather_df = weather_df.loc[:,['日期','天气状况','气温','holiday']]
    weather_df['最高温度'] = [item[:2] for item in weather_df['气温']]
    weather_df['最低温度'] = [item[-3:-1] for item in weather_df['气温']]
    weather_df['平均温度'] = [strGetAve(item[:2],item[-3:-1]) for item in weather_df['气温']]
    weather_df['周几'] = [get_week_day(st) for st in weather_df['日期']]
    filelist=os.listdir('datasets')
    dayLists = []
    i = 0
    for item in filelist:
        dayList = []
        dayList.append(item[:-4])
        filename = 'datasets/' + item
        raw_train_df = read_csv(filename)
        dayList.append(raw_train_df.shape[0])
        dayList.append(weather_df['天气状况'][i])
        dayList.append(weather_df['周几'][i])
        dayList.append(weather_df['最高温度'][i])
        dayList.append(weather_df['最低温度'][i])
        dayList.append(weather_df['平均温度'][i])
        dayList.append(weather_df['holiday'][i])
        i += 1
        dayLists.append(dayList)   
    result = '[\n'
    for item in dayLists:
        print ('dealing--------:' + str(item[0]))
        if str(item[7]) == '0':
            result = result + '    [\n        \"' + str(item[0]) +'\",\n        ' + str(item[1]) + ',\n        \"' + str(item[2]) + '\",\n        \"' + str(item[3]) + '\",\n        \"' + str(item[4]) + '\",\n        \"' + str(item[5]) + '\",\n        \"' + str(item[6]) + '\",\n        \"' + '\"\n    ],\n'
        else:
            result = result + '    [\n        \"' + str(item[0]) +'\",\n        ' + str(item[1]) + ',\n        \"' + str(item[2]) + '\",\n        \"' + str(item[3]) + '\",\n        \"' + str(item[4]) + '\",\n        \"' + str(item[5]) + '\",\n        \"' + str(item[6]) + '\",\n        \"' + str(item[7]) + '\"\n    ],\n'
    file = open('calendarHeatMap.json','w', encoding="utf-8")
    file.write(result[:-2]+'\n]')
    file.close()
    
def readTxt(filename):
    pos = []

    with open(filename, 'r', encoding='utf-8') as file_to_read:
        while True:
            lines = file_to_read.readline() # 整行读取数据
            if not lines:
                break
                pass
            p_tmp = [i for i in lines.split(',')] # 将整行数据分割处理，如果分割符是空格，括号里就不用传入参数，如果是逗号， 则传入‘，'字符。
            pos.append(p_tmp)  # 添加新读取的数据
            pass          
    return pos


    
def RealtimeStatistics(foldername): 
    filelist=os.listdir('datasets')
    realtimeStati = []
    for item in filelist:
        print ('dealing>>>>>', item)
        dayList = []
        dayList.append(item[:-4])
        filename = 'datasets/' + item
        
        pos = readTxt(filename)
        pos = pos[1:]
        pos = DataFrame(pos)
        pos = pos.drop([1], axis=1)
        pos.columns = ['order_id','product_id','type','combo_type','traffic_type','passenger_count', 'driver_product_id', 'start_dest_distance', 'arrive_time', 'departure_time', 'pre_total_fee', 'normal_time', 'bubble_trace_id', 'product_1level', 'year', 'month', 'day', 'starting_lng', 'starting_lat', 'dest_lng', 'dest_lat']
        pos['passenger_count'] = [float(item)/1000 for item in pos['passenger_count']]
        pos['normal_time'] = ['0' if str(item) == '' else item for item in pos['normal_time']]
        
        pos['changtu'] = [1 if item > 30 or item == 30 else 0 for item in pos['passenger_count']]
        result1 = np.round(pos['changtu'].sum()/(pos['passenger_count'].shape[0])*100,3)
        
        pos['kuaiche'] = [1 if str(item) == '3.0' else 0 for item in pos['product_1level']]
        result2 = np.round(pos['kuaiche'].sum()/(pos['kuaiche'].shape[0])*100,3)

        pos['gaojia'] = [1 if int(float(item)) > 60 or int(float(item)) == 60 else 0 for item in pos['pre_total_fee']]
        result3 = np.round(pos['gaojia'].sum()/(pos['pre_total_fee'].shape[0])*100,3)

        pos['changshi'] = [1 if int(float(item)) > 60 or int(float(item)) == 60 else 0 for item in pos['normal_time']]
        result4 = np.round(pos['changshi'].sum()/(pos['normal_time'].shape[0])*100,3)
 
        print (item[:-4], str(result1)+'%', str(result2)+'%', str(result3)+'%', str(result4)+'%')
        dayList.append(str(result1)+'%')
        dayList.append(str(result2)+'%')
        dayList.append(str(result3)+'%')
        dayList.append(str(result4)+'%')
        realtimeStati.append(dayList)
 
    file = open('RealtimeStatistics.json','w', encoding="utf-8")
    file.write(str(realtimeStati))
    file.close()   


def normalization2(data):
    _range = np.max(abs(data))
    return np.round(data / _range, 4)

def normalization(data):
    _range = np.max(data) - np.min(data)
    return (data - np.min(data)) / _range    

def standardization(data):
    mu = np.mean(data, axis=0)
    sigma = np.std(data, axis=0)
    return (data - mu) / sigma    
    
def Histogrammap(foldername):
    filelist=os.listdir('datasets')

    for item in filelist:
        print ('dealing>>>>>', item)
        dayList = []
        dayList.append(item[:-4])
        savefile = item[:-4]
        filename = 'datasets/' + item 
        pos = readTxt(filename)
        pos = pos[1:]
        pos = DataFrame(pos)
        pos = pos.drop([1], axis=1)
        pos.columns = ['order_id','product_id','type','combo_type','traffic_type','passenger_count', 'driver_product_id', 'start_dest_distance', 'arrive_time', 'departure_time', 'pre_total_fee', 'normal_time', 'bubble_trace_id', 'product_1level', 'year', 'month', 'day', 'starting_lng', 'starting_lat', 'dest_lng', 'dest_lat']

        pos['hour'] = [pd.to_datetime(item).hour for item in pos['departure_time']]
    
        num_hour = []
        
        groupedByHour = pos.groupby(['hour'])
        for group_name, group_data in groupedByHour:
            num_hour.append(group_data.shape[0])
        
        if len(num_hour) == 24:
        
            value_hour = []
            for i in range(len(num_hour)-1):
                value_hour.append(num_hour[i+1]-num_hour[i])
            value_hour = np.array(value_hour)
            value_hour = normalization2(value_hour)
            result = '[\n' 
            i = 1
            for item in value_hour:
                result = result + '    [\"' +str(i)+ '\",' + str(item) +'],\n'
                i += 1
            
            result = result[:-2] + '\n]'     
        else:
            result = '[\n'
            
            i = 1
            for item in value_hour:
                result = result + '    [\"' +str(i)+ '\",' + str(0) +'],\n'
                i += 1
            result = result[:-2] + '\n]'
        filePath = 'Histogrammap/'+savefile+'.json'
        file = open(filePath,'w', encoding="utf-8")
        file.write(result)
        file.close()       
    
    
def dayOrder(foldername):
    filelist=os.listdir(foldername)
    dayLists = []
    for item in filelist: 
        print ('dealing---:', item)
        dayList = []
        dayList.append(item[:-4])
        filename = 'datasets/' + item
        raw_train_df = read_csv(filename)
        dayList.append(raw_train_df.shape[0])
        dayLists.append(dayList)
    fileSave = 'dayOrder.csv'  
    df = pd.DataFrame(dayLists, columns=['date','order']) 
    df.to_csv(fileSave, encoding='utf_8_sig')
    



def IsPtInPoly(aLon, aLat, pointList):
    '''
    :param aLon: double 经度
    :param aLat: double 纬度
    :param pointList: list [(lon, lat)...] 多边形点的顺序需根据顺时针或逆时针，不能乱
    '''
    iSum = 0
    iCount = len(pointList)
    
    if(iCount < 3):
        return False
    
    
    for i in range(iCount):
        
        pLon1 = pointList[i][0]
        pLat1 = pointList[i][1]
        
        if(i == iCount - 1):
            
            pLon2 = pointList[0][0]
            pLat2 = pointList[0][1]
        else:
            pLon2 = pointList[i + 1][0]
            pLat2 = pointList[i + 1][1]
        
        if ((aLat >= pLat1) and (aLat < pLat2)) or ((aLat>=pLat2) and (aLat < pLat1)):
            
            if (abs(pLat1 - pLat2) > 0):
                
                pLon = pLon1 - ((pLon1 - pLon2) * (pLat1 - aLat)) / (pLat1 - pLat2);
                
                if(pLon < aLon):
                    iSum += 1
 
    if(iSum % 2 != 0):
#        print ('in it!')
        return True
    else:
#        print (' not in it!')
        return False    
    

#def dayAreaOrder(foldername):
#    filelist=os.listdir(foldername)
#    pointList = [(110.321053,20.022773), (110.325291,20.02369), (110.325999,20.020626), (110.321825,20.019255)]
#    for item in filelist:
#        print (item)
#        filename = item[:-4]
#        filepath = 'datasets/'+item 
#        
#        raw_train_df = read_csv(filepath)    
#        raw_train_df['hour'] = [pd.to_datetime(item).hour for item in raw_train_df['departure_time']]
#        
#        list_all_order = []
#        
#        all_hour = raw_train_df['hour'].unique()
#        if len(all_hour) == 24:
#                    
#            groupedByHour = raw_train_df.groupby(['hour'])
#
#            hour_order = []
#            hour_order.append(filename)
#            for group_name, group_data in groupedByHour:
#                print ('处理数据的时间段：', filename, group_name)
#                print (group_data.shape)
#                
#                
#                
#                for item in group_data:
#                    print (item) 
##                pandingbiao = [1 if IsPtInPoly(aLon, aLat, pointList) else 0 for aLon in group_data['starting_lng'] for aLat in group_data['starting_lat']]
#
##                print (group_data['starting_lng'], group_data['starting_lat'])
##                print (sum(pandingbiao), len(pandingbiao))

if __name__ == '__main__':
    
#桑葚图    
    filelist=os.listdir('dataset')
    for item in filelist:
        print (item)
        filepath = 'dataset/'+item
        
        orderNum, list_address = processJson(filepath)
        
        print (orderNum)
        print (len(list_address))
        
        print (list_address[:10])
        
        print ('-----------------------')


#        dataSta(list_address, item[:-5])
        hexiantu(list_address, item[:-5])

##每天 24小时的订单数
#    filename = '2017-05-13'
#    filepath = 'datasets/'+filename+'.txt'    
#    orderNumByHour(filepath, filename)
    
    
##3D热力图
#    filelist=os.listdir('datasets')
#    for item in filelist:
#        print (item)
#        filename = item[:-4]
#        filepath = 'datasets/'+filename+'.txt' 
#        thermodynamicByHour(filepath, filename)
        

#日历热力图
#     foldername = 'datasets'
#     calendarHeatMap(foldername)
                
        
##实时统计
#     foldername = 'datasets'
#     RealtimeStatistics(foldername)        

#柱状图
#     foldername = 'datasets'
#     Histogrammap(foldername) 


##day order
#     foldername = 'datasets'
#     dayOrder(foldername)


###每天 24小时的订单数
#    filelist=os.listdir('datasets')
#    for item in filelist:
#        print (item)
#        filename = item[:-4]
#        filepath = 'datasets/'+item    
#        orderNumByHour(filepath, filename)


    
    
##订单量预测处理    
##110.321053,20.022773 （左上）
##110.325291,20.02369 （右上）
##110.321825,20.019255 （左下）
##110.325999,20.020626 （右下）
#    
#    foldername = 'datasets'
#    dayAreaOrder(foldername)
    




    
    
    
    
    
    