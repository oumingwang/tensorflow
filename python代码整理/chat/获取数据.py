#coding:utf8
import itchat
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

itchat.login()
friends = itchat.get_friends(update=True)[0:]
print friends

male = female = other = 0

sexList = []
userList = []
for i in friends[1:]:
    sex = i['Sex']
    if sex == 1:
        sexList.append('male')
    elif sex == 2:
        sexList.append('female')
    else:
        sexList.append('other')

total = len(friends[1:])

#print "male: %.2f%%" % (float(male)/total*100)
#print "female: %.2f%%" % (float(female)/total*100)
#print "other: %.2f%%" % (float(other)/total*100)


print userList
df = pd.DataFrame(sexList,columns = ['sex'])

print df

plt.figure(figsize=(12,8))
sns.countplot(x = df['sex'])
plt.show()

