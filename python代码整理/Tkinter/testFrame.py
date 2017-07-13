# encoding: utf-8
# !/usr/bin/python

'''''Tkinter教程之Frame篇'''
# Frame就是屏幕上的一块矩形区域，多是用来作为容器（container）来布局窗体。
'''''1.创建Frame'''
# -*- coding: cp936 -*-
from Tkinter import *

root = Tk()
# 以不同的颜色区别各个frame
for fm in ['red', 'blue', 'yellow', 'green', 'white', 'black']:
    # 注意这个创建Frame的方法与其它创建控件的方法不同，第一个参数不是root
    Frame(height=200, width=400, bg=fm).pack()
root.mainloop()
# 添加不同颜色的Frame，大小均为20*400


'''''2.向Frame中添加Widget'''
# -*- coding: cp936 -*-
from Tkinter import *
root = Tk()
fm = []
#以不同的颜色区别各个frame
for color in ['red','blue']:
    #注意这个创建Frame的方法与其它创建控件的方法不同，第一个参数不是root
    fm.append(Frame(height = 200,width = 400,bg = color))
#向下面的Frame中添加一个Label
Label(fm[1],text = 'Hello label').pack()
Label(fm[0],text = 'Hello label').pack()
fm[0].pack()
fm[1].pack()
root.mainloop()
#Label被添加到下面的Frame中了，而不是root默认的最上方。
#大部分的方法来自gm,留到后面gm时再介绍


from Tkinter import *
root = Tk()
for lf in ['red','blue','yellow']:
    #可以使用text属性指定Frame的title
    LabelFrame(height = 200,width = 300,text = lf, bg = lf).pack()
root.mainloop()