import tkinter as tk
from tkinter import messagebox
  
#设置窗口居中
def window_info():
 ws = window.winfo_screenwidth()
 hs = window.winfo_screenheight()
 x = (ws / 2) - 200
 y = (hs / 2) - 200
#  print("%d,%d" % (ws, hs))
 return x,y
  
#设置登陆窗口属性
window = tk.Tk()
window.title('we-get')
a,b=window_info()
window.geometry("450x300+%d+%d"%(a,b))
  
#登陆界面的信息
# tk.Label(window,text="we-get下载",font=("宋体",32)).place(x=80,y=50)
tk.Label(window,text="地址：").place(x=50,y=50)
tk.Label(window,text="名称：").place(x=120,y=100)
#显示输入框
var_address = tk.StringVar()
#显示默认地址
# var_address.set('1400370101')
entry_address=tk.Entry(window,textvariable=var_address)
entry_address.place(x=190,y=50)

var_name = tk.StringVar()
#设置输入密码后显示*号
var_name.set('默认名称')
entry_name = tk.Entry(window,textvariable=var_name)
entry_name.place(x=190,y=100)
  
#登陆函数
# def usr_down():
#  #获取输入的账号密码
#  address = var_address.get()
#  name = var_name.get()
#  #获取存储的账户信息，此处使用的是数据库，调用数据库查询函数，也可以使用其他方式，如文件等
#  dicts = SQL.load('down')
#  print(dicts)
#  bool = False
#  for row in dicts:
#   print(row.get("name"))
#  if address == row["name"]:
#   bool = True
#   pwd = row["password"]
#   print(row)
#  if bool == True:
#   if name == pwd:
#    tk.messagebox.showinfo(title='Welcome', message='How are you?' +address)
#   #  mainwindow()
#   else:
#    tk.messagebox.showerror(message='对不起，输入错误，请重试！')
#  else:
#   is_sign_up = tk.messagebox.askyesno('Welcome', '您还没有注册，是否现在注册呢？')
#  if is_sign_up:
#   usr_sign_up()
#注册账号
# def usr_sign_up():
#  def sign_to_Pyhon():
#   np = new_pwd.get()
#   npc = new_pwd_confirm.get()
#   nn = new_name.get()
  
#  dicts = SQL.load('down')
#  print(dicts)
#  bool = False
#  for row in dicts:
#   if nn == row["name"]:
#    bool = True
#    print(row)
#  if np!=npc:
#   tk.messagebox.showerror('对不起','两次密码输入不一致！')
#  elif bool:
#   tk.messagebox.showerror(('对不起','此账号已经存在!'))
#  else:
#   try:
#    SQL.insert_down(str(nn),str(np))
#    tk.messagebox.showinfo('Welcome','您已经注册成功！')
#   except:
#    tk.messagebox.showerror(('注册失败!'))
#    window_sign_up.destroy()
#  #创建top窗口作为注册窗口
#  window_sign_up = tk.Toplevel(window)
#  window_sign_up.geometry('350x200')
#  window_sign_up.title('注册')
  
#  new_name = tk.StringVar()
#  new_name.set('1400370115')
#  tk.Label(window_sign_up,text='账号:').place(x=80,y=10)
#  entry_new_name = tk.Entry(window_sign_up,textvariable=new_name)
#  entry_new_name.place(x=150,y=10)
  
#  new_pwd = tk.StringVar()
#  tk.Label(window_sign_up, text='密码:').place(x=80, y=50)
#  entry_name = tk.Entry(window_sign_up,textvariable=new_pwd,show='*')
#  entry_name.place(x=150, y=50)
  
#  new_pwd_confirm = tk.StringVar()
#  tk.Label(window_sign_up,text='再次输入:').place(x=80,y=90)
#  entry_name_again = tk.Entry(window_sign_up,textvariable=new_pwd_confirm,show='*')
#  entry_name_again.place(x=150, y=90)
  
#  btn_again_sign_up = tk.Button(window_sign_up,text='注册',command=sign_to_Pyhon)
#  btn_again_sign_up.place(x=160,y=130)

def do_down():
    print('进行下载')
    address = var_address.get()
    name = var_name.get()
    print('下载地址：'+ address)
    print('名称：'+ name)
    
#登陆和注册按钮
btn_down = tk.Button(window,text="登陆",command=do_down)
btn_down.place(x=200,y=130)

# btn_sign_up = tk.Button(window,text="注册",command=usr_sign_up)
# btn_sign_up.place(x=270,y=230)
  
window.mainloop()