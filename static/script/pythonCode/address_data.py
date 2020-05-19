# -*- coding: utf-8 -*-
"""

@author: LeeZChuan


"""

import pandas as pd
import numpy as np
import requests
import os
from pandas.core.frame import DataFrame

pd.set_option('display.max_columns',1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth',1000)

def read_csv(filename):
    subfile = 'datasets2/'
    name_title = filename[:-3]
    fileInfo = subfile+filename
#    raw_train_df = pd.read_csv(fileInfo, sep='\s+', engine='python').loc[:,[name_title+'arrive_time',name_title+'starting_lng',name_title+'starting_lat',name_title+'dest_lng',name_title+'dest_lat']]
    raw_train_df = pd.read_csv(fileInfo, sep='\s+', engine='python')
    return raw_train_df


def locatebyLatLng(lat, lng, pois=0):
    '''
    根据经纬度查询地址
    '''
    items = {'location': str(lat) + ',' + str(lng), 'ak': 'fFYPupo84cWdICPUbxXkb9GYww0VYD5Y', 'output': 'json'}
    res = requests.get('http://api.map.baidu.com/geocoder/v2/', params=items)
    result = res.json()
#    print(result)
#    print('--------------------------------------------')
    #result = result['result']['formatted_address'] + ',' + result['result']['sematic_description']
    city = result['result']['addressComponent']['city']
    district = result['result']['addressComponent']['district']
    street = result['result']['addressComponent']['street']
    return city, district, street



def groupByDay(raw_df):
    groupedByDate = raw_df.groupby([name_title+'arrive_time'])

    
    for group_name, group_data in groupedByDate:
        data_one_date = []
        date = str(group_name)
        print ("dealing-------"+date)
        print (group_data.shape)
        for index, item in group_data.iterrows():
            data_each_line = []        
            data_each_line.append(item[name_title+'starting_lng'])
            data_each_line.append(item[name_title+'starting_lat'])
            data_each_line.append(item[name_title+'dest_lng'])
            data_each_line.append(item[name_title+'dest_lat'])
            data_one_date.append(data_each_line)

        df = pd.DataFrame(data_one_date, columns=['starting_lng', 'starting_lat', 'dest_lng', 'dest_lat']) 
        fileInfo = 'datasets/'+date+'.txt'
        df.to_csv(fileInfo, encoding='utf_8_sig')
        

def groupByDay2(raw_df):
    groupedByDate = raw_df.groupby([name_title+'arrive_time'])

    
    for group_name, group_data in groupedByDate:
        data_one_date = []
        date = str(group_name)
        print ("dealing-------"+date)
        print (group_data.shape)
        for index, item in group_data.iterrows():
            data_each_line = []
            data_each_line.append(item[name_title+'order_id'])
            data_each_line.append(item[name_title+'product_id'])
            data_each_line.append(item[name_title+'type'])
            data_each_line.append(item[name_title+'combo_type'])
            data_each_line.append(item[name_title+'traffic_type'])
            data_each_line.append(item[name_title+'passenger_count'])
            data_each_line.append(item[name_title+'driver_product_id'])
            data_each_line.append(item[name_title+'start_dest_distance'])
            data_each_line.append(item[name_title+'arrive_time'])
            data_each_line.append(item[name_title+'departure_time'])
            data_each_line.append(item[name_title+'pre_total_fee'])
            data_each_line.append(item[name_title+'normal_time'])
            data_each_line.append(item[name_title+'bubble_trace_id'])
            data_each_line.append(item[name_title+'product_1level'])
            data_each_line.append(item[name_title+'year'])
            data_each_line.append(item[name_title+'month'])
            data_each_line.append(item[name_title+'day'])
            data_each_line.append(item[name_title+'starting_lng'])
            data_each_line.append(item[name_title+'starting_lat'])
            data_each_line.append(item[name_title+'dest_lng'])
            data_each_line.append(item[name_title+'dest_lat'])
            data_one_date.append(data_each_line)
            
            

        df = pd.DataFrame(data_one_date, columns=['order_id','product_id','type','combo_type','traffic_type','passenger_count', 'driver_product_id', 'start_dest_distance', 'arrive_time', 'departure_time', 'pre_total_fee', 'normal_time', 'bubble_trace_id', 'product_1level', 'year', 'month', 'day', 'starting_lng', 'starting_lat', 'dest_lng', 'dest_lat']) 
        fileInfo = 'datasets/'+date+'.txt'
        df.to_csv(fileInfo, encoding='utf_8_sig')    
        

def groupByDay3(raw_df):
    groupedByDate = raw_df.groupby([name_title+'arrive_time'])

    
    for group_name, group_data in groupedByDate:
        date = str(group_name)
        print ("dealing-------"+date)
        print (group_data.shape)
        data_one_date = []
        
        for index, item in group_data.iterrows():
            data_each_line = []
            data_each_line.append(item[name_title+'order_id'])
            data_each_line.append(item[name_title+'product_id'])
            data_each_line.append(item[name_title+'city_id'])
            data_each_line.append(item[name_title+'district'])
            data_each_line.append(item[name_title+'county'])
            data_each_line.append(item[name_title+'type'])
            data_each_line.append(item[name_title+'combo_type'])
            data_each_line.append(item[name_title+'traffic_type'])
            data_each_line.append(item[name_title+'passenger_count'])
            data_each_line.append(item[name_title+'driver_product_id'])
#            data_each_line.append(item[name_title+'start_dest_distance'])
            data_each_line.append(item[name_title+'arrive_time'])
#            data_each_line.append(item[name_title+'departure_time'])
            data_each_line.append(item[name_title+'pre_total_fee'])
            data_each_line.append(item[name_title+'normal_time'])
            data_each_line.append(item[name_title+'bubble_trace_id'])
            data_each_line.append(item[name_title+'product_1level'])
            data_each_line.append(item[name_title+'year'])
            data_each_line.append(item[name_title+'month'])
            data_each_line.append(item[name_title+'day'])
            data_each_line.append(item[name_title+'starting_lng'])
            data_each_line.append(item[name_title+'starting_lat'])
            data_each_line.append(item[name_title+'dest_lng'])
            data_each_line.append(item[name_title+'dest_lat'])
            data_one_date.append(data_each_line)
        
        

        df = pd.DataFrame(data_one_date, columns=['city_id','district', 'county', 'type','combo_type','traffic_type','passenger_count', 'driver_product_id', 'start_dest_distance', 'arrive_time', 'departure_time', 'pre_total_fee', 'normal_time', 'bubble_trace_id', 'product_1level', 'year', 'month', 'day', 'starting_lng', 'starting_lat', 'dest_lng', 'dest_lat'])
        fileInfo = 'datasets2/'+date+'.txt'
        df.to_csv(fileInfo, encoding='utf_8_sig') 
        
        
        

def streetNamefind(filename):
    subfile = 'datasets/'+filename[:-1]
    raw_train_files = os.listdir(subfile)
    for eachFile in raw_train_files[1037:]:
        raw_file_df = pd.read_csv(subfile+'/'+eachFile, engine='python').loc[:,['starting_lng', 'starting_lat', 'dest_lng', 'dest_lat']]
        print ('streetNameFind--'+eachFile)
        streetNames = []
        i = 1
        for index, item in raw_file_df.iterrows():
            streetName = []
            _, _, s_street = locatebyLatLng(item['starting_lat'], item['starting_lng'], pois=0)
            streetName.append(s_street)
            _, _, d_street = locatebyLatLng(item['dest_lat'], item['dest_lng'], pois=0)
            streetName.append(d_street)
            print (eachFile, '---', i, '   ---starting--', s_street, 'dest--', d_street)
            streetNames.append(streetName)
            i += 1
        
        df_street = pd.DataFrame(streetNames, columns=['starting_street', 'dest_street'])
        fileInfo = 'datasets/'+name_title[:-1]+'/'+eachFile[:-4]+'.txt'
        df_street.to_csv(fileInfo, encoding='utf_8_sig')    


def fileCut(filename):
    subfile = 'datasets/'+filename[:-1]
    raw_train_files = os.listdir(subfile)
    print (subfile, raw_train_files)
    for eachFile in raw_train_files:
        raw_file_df = pd.read_csv(subfile+'/'+eachFile, engine='python').loc[:,['starting_lng', 'starting_lat', 'dest_lng', 'dest_lat']]
        i = 0
        j = 1
        len_data = raw_file_df.shape[0]
        coordinatesNames = []
        for index, item in raw_file_df.iterrows():
            coordinatesName = []
            coordinatesName.append(item['starting_lng'])
            coordinatesName.append(item['starting_lat'])
            coordinatesName.append(item['dest_lng'])
            coordinatesName.append(item['dest_lat'])
            coordinatesNames.append(coordinatesName)
            i += 1
            if i%30==0 or i==len_data:
                df_coordinate = pd.DataFrame(coordinatesNames, columns=['starting_lng', 'starting_lat', 'dest_lng', 'dest_lat'])
                fileInfo = 'datasets/'+name_title[:-1]+'/'+str(j).zfill(4)+'.txt'
                print ('dealing--' + fileInfo)
                df_coordinate.to_csv(fileInfo, encoding='utf_8_sig') 
                coordinatesNames = []
                j += 1
                
        




def fileMerge(filename):
    subfile = 'datasets/'+filename[:-1]
    raw_train_files = os.listdir(subfile)
    saveFile = subfile+'/all_data.txt'
    i = 1
    for eachFile in raw_train_files:
        filename = subfile+'/'+eachFile
        print ("processing : " + filename)
        if i == 1:
            filecon = pd.read_csv(filename, header=0)
#            filecon = pd.read_csv(filename, header=None)
        else:
            filecon = pd.read_csv(filename)
            i += 1
        filecon.to_csv(saveFile, mode='a', index=False, header=False, encoding='utf_8_sig')
    

def dataSta(filename):
    subfile = 'datasets/'+filename[:-1]
    fileName = subfile+'/all_data.txt'
    raw_file_df = pd.read_csv(fileName, engine='python', encoding='utf_8_sig').loc[:,['starting_street', 'dest_street']]
    raw_file_df.dropna(axis=0, how='any', inplace=True) #删除含有空值的行
    result = raw_file_df.groupby([raw_file_df['starting_street'],raw_file_df['dest_street']])
    
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
    name_df = name_df[0].unique()
    name_list = name_df.tolist()
    
    print (name_list)

    strValue = "data:["
    for item in name_list:
        strValue = strValue+"{name:'"+item+"'},"
    strValue = strValue[:-1]
    strValue = strValue + "],\n"
        
    strValue = strValue + "links:["
    for item in all_result:
        strValue = strValue+"{source:'"+item[0]+"', target:'"+item[1]+"', value:"+str(item[2])+"},"
    
    strValue = strValue[:-1]
    strValue = strValue + "]"

    
#    path = os.getcwd()+'\dataForMulberryFigure\\'+filename[:-1]+'.txt'
    name_path = os.getcwd()+'\dataForMulberryFigure\\'+filename[:-1]+'_nodes_links.txt'
#    a = open(path, "w",encoding='UTF-8')
#    a.write(str(all_result))
#    a.close()
    
    def save(filename, contents):
        fh = open(filename, 'w', encoding='utf-8')
        fh.write(contents)
        fh.close()
    save(name_path, strValue)


if __name__ == '__main__':
    filename = "dwv_order_make_haikou_8.txt"
    name_title = filename[:-3] 

    
    
##按日期划分数据集
#    raw_df = read_csv(filename)
#    
##    print (raw_df.head(2))
#    
#    raw_df[name_title+'arrive_time'] = pd.to_datetime(raw_df[name_title+'arrive_time'],format="%Y-%m-%d").dt.date
#    raw_df = raw_df[~(raw_df[name_title+'arrive_time']=='0000-00-00')]
#    groupByDay3(raw_df)


#坐标转换                
#    streetNamefind(name_title)
    
##分批坐标转换
#  1. 切分文件
#    fileCut(name_title)
#  #2. 坐标转换
#    streetNamefind(name_title)
  #3. 文件合并
#    fileMerge(name_title)
  
  #4. 统计及格式操作
#    dataSta(name_title)

        
        


									