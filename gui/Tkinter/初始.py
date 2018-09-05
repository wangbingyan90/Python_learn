import tkinter

top = tkinter.Tk()

li     = ['C','python','php','html','SQL','java']
movie  = ['CSS','jQuery','Bootstrap']
listb  = tkinter.Listbox(top)
listb2 = tkinter.Listbox(top)

for item in li:                 # 第一个小部件插入数据
    listb.insert(0,item)
for item in movie:              # 第二个小部件插入数据
    listb2.insert(0,item)

listb.pack()                    # 将小部件放置到主窗口中
listb2.pack()


top.mainloop()