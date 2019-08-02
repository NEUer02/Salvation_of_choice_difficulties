# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 18:20:15 2019

@author: Pang Hanyu
@student number: 20161858
"""

from tkinter import *
from tkinter import ttk

class GressBar():

    def start(self):
        top = Toplevel()
        self.master = top
        top.overrideredirect(True)
        top.title("进度条")
        Label(top, text="任务正在运行中,请稍等……", fg="green").pack(pady=2)
        prog = ttk.Progressbar(top, mode='indeterminate', length=200)
        prog.pack(pady=10, padx=35)
        prog.start()

        top.resizable(False, False)
        top.update()
        curWidth = top.winfo_width()
        curHeight = top.winfo_height()
        scnWidth, scnHeight = top.maxsize() 
        tmpcnf = '+%d+%d' % ((scnWidth - curWidth) / 2, (scnHeight - curHeight) / 2)
        top.geometry(tmpcnf)
        top.mainloop()

    def quit(self):
        if self.master:
            self.master.destroy()
