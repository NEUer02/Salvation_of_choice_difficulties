# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 13:55:56 2019

@author: Pang Hanyu
@student number: 20161858
"""

import tkinter as tk
import random as rm

flag=None
txt=[]

def buttonfuction():
    window.destroy()
    
    number=rm.randint(0,len(txt)-1)
    
    window_finish=tk.Tk()
    window_finish.title('结果是！！！')
    window_finish.geometry('200x280')
    show=tk.Frame(window_finish)
    show.grid()
    
    message='决定就是它了！   ! '+txt[number]+' ！'
    
    label_x=tk.Label(show,text=message) #创建label
    label_x.grid(row='0',column='0')
    
    photo=tk.PhotoImage(file='hand.gif')
    label_2=tk.Label(show,image=photo)
    label_2.grid(row='1',column='0')
    
    btn_finish=tk.Button(show,text = "！奥里给！",command=finish_fuction()) #创建按钮
    btn_finish.grid(row='2',column='0',padx=200,pady=10)
    
    window_finish.mainloop()

def showfuction():
    txt.append(entry.get())
    string.set('')

def finish_fuction():
    window_finish.destroy()
    

# 设置窗口
window = tk.Tk()  # 建立一个窗口
window.title('帮你做决定~')
window.geometry('400x100')

app=tk.Frame(window) #app放置在window里面
app.grid() #放置app

label=tk.Label(app,text="请输入你犹豫不决的事情能做的选项：") #创建label
label.grid(row='0',column='1')

string=tk.StringVar()
entry=tk.Entry(app,textvariable=string)#创建输入框
string.set("")
entry.grid(row='1',column='1')

label_show=tk.Label(app,text=entry.get()) #创建label
label_show.grid(row='2',column='1')

btn_show=tk.Button(app,text = "加入选项",command=showfuction) #创建按钮
btn_show.grid(row='3',column='0')

btn_quit=tk.Button(app,text = "完成输入请点击这里",command=buttonfuction) #创建按钮
btn_quit.grid(row='3',column='2')

window.mainloop()