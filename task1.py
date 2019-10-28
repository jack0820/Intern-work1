# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 23:04:16 2019

@author: Jack Qi
"""

import pandas as pd

'''导入数据文件'''
data = pd.read_csv('file1.csv',encoding = 'GBK')
order_id = data['订单号']
seller_id = data['设备ID']
need_price = data['应付金额']
paid_price = data['实际金额']
product = data['商品']
paid_time = data['支付时间']
site = data['地点']
condition = data['状态']
cash = data['提现'] 


'''将数据写入CSV'''
data_a = data[data['地点'].str.contains('A')]
data_b = data[data['地点'].str.contains('B')]
data_c = data[data['地点'].str.contains('C')]
data_d = data[data['地点'].str.contains('D')]
data_e = data[data['地点'].str.contains('E')]

data_a.to_csv('task1-1A.csv',index=False,encoding="utf_8_sig")
data_b.to_csv('task1-1B.csv',index=False,encoding="utf_8_sig")
data_c.to_csv('task1-1C.csv',index=False,encoding="utf_8_sig")
data_d.to_csv('task1-1D.csv',index=False,encoding="utf_8_sig")
data_e.to_csv('task1-1E.csv',index=False,encoding="utf_8_sig")




#计算每台售货机一年的交易额
suoyin = [data_a,data_b,data_c,data_d,data_e]
for i in suoyin:
    print(i['实际金额'].sum())
    
#计算每台售货机的每年订单量
for i in suoyin:
    print('售货机的一年订单量为：',len(i))
##备用方法
'''print(data_a['实际金额'].sum(),',',
      data_b['实际金额'].sum(),',',
      data_c['实际金额'].sum(),',',
      data_d['实际金额'].sum(),',',
      data_e['实际金额'].sum())'''

##其余操作在excel上完成
