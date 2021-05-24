'''DataITO模块'''
'''Python数据输入(Input)、转换(transform)、输出(output)，一行代码读取/转换多种格式的数据文件'''

import os
import numpy as np
import pandas as pd


'''输入(input):数据读取'''
def read(path):

    DataFormat = path.split(".")[1] #获取文件后缀

    if DataFormat == 'xlsx':
        data = pd.read_excel(path,engine='openpyxl')
        return data

    data = {
        'txt': open(path, "r",encoding='utf-8'),
        'csv': pd.read_csv(path),
        # 'xlsx': pd.read_excel(path,engine='openpyxl') #这个比较离谱，放在这里就会报错
    }.get(DataFormat,"error, unsupported format")

    return data


'''转换(transform):格式转换'''
def transform(basic_data,target_data_type):

    data = {
        'dataframe': pd.DataFrame(basic_data),   #转换为dataframe类型
        # 'list': basic_data.values.tolist(),
    }.get(target_data_type,"error, unsupported format")
    return data


'''输出:数据保存'''
def save(data,savepath = " ",savename = "data.xlsx"):

    data = transform(data,'dataframe')

    if isinstance(data,pd.DataFrame):
        if savepath == " ":
            data.to_excel(savename)
        else:
            data.to_excel( savepath + "\\" + savename)
    else:
        print("error, unsupported format")





