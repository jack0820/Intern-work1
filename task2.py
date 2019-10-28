# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 23:04:16 2019

@author: Jack Qi
"""


'''数据分析与可视化'''
#绘制5台售货机总销量商品top10
import pandas as pd
data = pd.read_csv('file1.csv',encoding = 'GBK')
print(data['商品'].value_counts()[:10])


##计算毛利率
import pandas as pd

file1 = pd.read_csv('file1.csv',encoding='GBK')

def get_ylprofit(k):
 #   for i in ('A','B','C','D','E'):
        ff = file1[file1['地点']==k]
        ffyl = ff[ff['keyword']=='饮料']
        fflr = ffyl['实际金额'].sum() * 0.25 #计算饮料类毛利率
        return fflr
    
def get_fylprofit(k):
    ff = file1[file1['地点']==k]
    ffyl = ff[ff['keyword']=='饮料']
    fflr = ffyl['实际金额'].sum() * 0.2 #计算非饮料类毛利率
    return fflr


suoyin1 = ['A','B','C','D','E']


ylml = [0,0,0,0,0]
for i in range(5):
    ylml[i] = get_ylprofit(suoyin1[i])
    
    
fylml = [0,0,0,0,0]
for i in range(5):
    fylml[i] = get_fylprofit(suoyin1[i])   

print(ylml,fylml)

##其余图表和操作在excel上完成