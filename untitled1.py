# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 16:26:01 2019

@author: Pang Hanyu
@student number: 20161858
"""

from tkinter import *

def onclick():
    print("onclick !!!")

root = Tk()

#实例化Button，使用command选项关联一个函数，点击按钮则执行该函数
button = Button(root,text='这是一个按钮',fg='red',command=onclick)

#设置pack布局方式
button.pack()

root.mainloop()
