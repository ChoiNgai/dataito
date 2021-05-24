'''DataITO模块'''
'''Python数据输入(Input)、转换(transform)、输出(output)，一行代码读取/转换多种格式的数据文件'''

import os
import numpy as np
import pandas as pd

def read(path):
    DataFormat = path.split(".")[1] #获取文件后缀

    if DataFormat  == 'txt':
        data = open(path, "r",encoding='utf-8')
    elif DataFormat  == 'csv':
        data = pd.read_csv(path)
    elif DataFormat == 'xlsx':
        data = pd.read_excel(path,engine='openpyxl')
    else:
        print("error, unsupported format")

    return data

def transform(basic_data,target_data_type):
    if target_data_type == 'dataframe': #转换为dataframe类型
        data = pd.DataFrame(basic_data)
    # if target_data_type == '':
    return data
