#coding:utf8
import itchat
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

itchat.login()
friends = itchat.get_friends(update=True)[0:]
print friends
#np.savetxt('data.txt',friends)


def get_var(var):
    variable = []
    for i in friends:
        value = i[var]
        variable.append(value.encode('utf-8'))
    return variable

def get_var1(var):
    variable = []
    for i in friends:
        value = i[var]
        variable.append(value)
    return variable
NickName = get_var("NickName")
Sex = get_var1('Sex')
Province = get_var('Province')
City = get_var('City')
Signature = get_var('Signature')


data = {"NickName":NickName,'Sex':Sex,'Province':Province,'City':City,'Signature':Signature}

frame = pd.DataFrame(data,dtype=object)
print frame
frame.to_csv('data.csv',index=True)