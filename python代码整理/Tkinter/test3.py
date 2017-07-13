from Tkinter import *



root = Tk()
v = IntVar()
v.set(1)
def sel():
    print str(v.get())
for i in range(3):
    Radiobutton(root,
                    variable = v,
                    indicatoron = 0,
                    text = 'python & tkinter',
                    value = i,
                    command =sel
                    ).pack()
root.mainloop()


