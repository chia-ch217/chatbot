# -*- coding: utf-8 -*-
"""
Created on Thu May  7 00:29:00 2020

@author: GIGABYTE
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import matplotlib


def data_predict(name,to_be):
    data = pd.read_excel('data.xlsx',encoding='utf8')
    data = data.set_index(data.Year)
    group = data.groupby(['Industry'])
    
    industrys = []  #產業
    hireds = [] #雇用人數
    sums  = [] #總薪資
    if name == '110' :
        n = '資訊系統分析及設計師'
    elif name == '129':
        n = '軟體開發及程式設計師'
    elif name == '209':
        n = '資料庫及網路專業人員'

    for value in group:
        industrys.append(value[0])
        hireds.append(value[1]['hired-{}'.format(name)])
        sums.append(value[1]['sum-{}'.format(name)])
        
    #跑預測
    for i in range(len(industrys)): 
        inds = industrys[i]      #產業
        hs = np.array(hireds[i]).reshape(-1,1) #雇用人數 
        sms = np.array(sums[i])  #總薪資 

        #轉換維度
        hs_2 = np.reshape(hs,(len(hs),1))
        sms_2 = np.reshape(sms,(len(sms),1))
        
        #線性迴歸
        lm = LinearRegression()
        lm.fit(hs_2,sms_2)
        
        #模型績效
        mse = np.mean((lm.predict(hs)-sms)**2)
        r_squared = lm.score(hs,sms)
        
        #輸入雇員人數
        to_be = np.array(to_be)
        p_sum = lm.predict(np.reshape(to_be,(len(to_be),1))) #預測薪水    
        
        #print('{}-{}-係數 = {}'.format(inds,n,lm.coef_))
        #print('{}-{}-截距 = {}'.format(inds,n,lm.intercept_))
        #print('{}-{}-mse = {}'.format(inds,n,mse))
        #print('{}-{}-r-squared = {}'.format(inds,n,r_squared))
        print(p_sum)
        
        '''
        #圖像化
        plt.figure(figsize=(10,5))
        plt.scatter(hs_2,sms_2,color = '#F87217')
        plt.plot(hs, lm.predict(hs),color='#169DF7',linewidth = 2)
        chinese_font = matplotlib.font_manager.FontProperties(fname="C:\Windows\Fonts\msjh.ttc")
        plt.title('100年至107年/{}/{}'.format(n,inds),fontproperties=chinese_font)
        plt.xlabel('雇用人數',fontproperties=chinese_font)
        plt.ylabel('薪資',fontproperties=chinese_font)
        plt.savefig('{}_{}.jpg'.format(inds,n))
        '''

to_be = 30

names = ['110','129','209']
#for n in names:
print(data_predict('110',to_be))
    