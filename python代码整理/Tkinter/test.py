#coding:utf8
from Tkinter import *
import tkMessageBox

root = Tk()
root.title('智能旅游助手')


def submit(str1):
    print str1.get()

def reset(str1):
    str1.set("")

str1 = StringVar()

L1 = Label(root, text="City Name")
L1.grid(row=0,column=0)

E1 = Entry(root, bd=5,textvariable=str1)
E1.grid(row=0,column=2)
B1 = Button(root, text ='确定', command = lambda : submit(str1) ).grid(row=1,column=1)
B2 = Button(root, text ='重置', command = lambda : reset(str1) ).grid(row=1,column=2)

#listb.pack()                    # 将小部件放置到主窗口中
#listb2.pack()

'''

fm1 = Frame(height=200, width=400)
label = Label(fm1, text="City Name").grid(row=0,column=0)
B1 = Button(fm1, text ='确定').grid(row=0,column=1)

fm1.pack()
'''
root.mainloop()
