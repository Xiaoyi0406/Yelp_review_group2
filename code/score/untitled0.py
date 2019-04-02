#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 23:57:01 2019

@author: kzhao46
"""

import pandas as pd
from word2vec import word_embedding
import config
import numpy as np
import Svm
import os


def find_score(word):
    X_text = []
    if word not in Word2vec:
        return None
    else:
        X_text.append(Word2vec[word])
        X_text = np.array(X_text)
        return svc.predict(X_text).tolist()[0]

'''
import pandas as pd
import os
Folder_Path = r'/Users/kzhao46/Dropbox/score/data'          #要拼接的文件夹及其完整路径，注意不要包含中文
SaveFile_Path =  r'/Users/kzhao46/Dropbox/score/data'       #拼接后要保存的文件路径
SaveFile_Name = r'all.csv'              #合并后要保存的文件名
 
#修改当前工作目录
os.chdir(Folder_Path)
#将该文件夹下的所有文件名存入一个列表
file_list = os.listdir()
  
#读取第一个CSV文件并包含表头
df = pd.read_csv(Folder_Path +'/'+ file_list[0])   #编码默认UTF-8，若乱码自行更改
 
#将读取的第一个CSV文件写入合并后的文件保存
df.to_csv(SaveFile_Path+'/'+ SaveFile_Name,encoding="utf_8_sig",index=False)
 
#循环遍历列表中各个CSV文件名，并追加到合并后的文件
for i in range(1,len(file_list)):
    df = pd.read_csv(Folder_Path + '/'+ file_list[i])
    df.to_csv(SaveFile_Path+'/'+ SaveFile_Name,encoding="utf_8_sig",index=False, header=False, mode='a+')

'''
"""
path = "/Users/kzhao46/Desktop/data/"
names = []
for file in os.listdir(path):
    file_path = os.path.join(path, file) 
    if os.path.splitext(file_path)[1] == '.csv':
        names.append(file_path)
for name in names:
    f=pd.read_csv(name)
    f['score_food']=f['food_JJ'].apply(lambda sen: [find_score(x) for x in str(sen).split()])
    f['score_service']=f['service_JJ'].apply(lambda sen: [find_score(x) for x in str(sen).split()])
    f['score_food']=f['score_food'].apply(lambda a: [])
    f.to_csv(name, index = False, encoding='utf-8')
"""
f=pd.read_csv('/Users/kzhao46/Dropbox/628-2/new data test/regional.csv')
f['score_food']=f['food_JJ'].apply(lambda sen: [find_score(x) for x in str(sen).split()])
print("food")
#f['score_service']=f['service_JJ'].apply(lambda sen: [find_score(x) for x in str(sen).split()])
#print('service')
f.to_csv('/Users/kzhao46/Desktop/data/out/regional.csv', index = False, encoding='utf-8')
