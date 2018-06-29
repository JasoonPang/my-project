# -*- coding: utf-8 -*-
# @Time    : 2018/6/29 12:11
# @Author  : JasoonPang
# @Email   : 724719274@qq.com


from tkinter import *    # 注意模块导入方式，否则代码会有差别

root = Tk()
d = {'汽车': {'发动机': 1, '轮胎': 2, '油缸': 3}}


def f(fm1, d={}):
    keys = list(d.keys())
    for i in keys:
        for j in d[i]:
            Button(fm1, text='{}  {}    {}'.format(i, j, d[i][j]), width=30).pack(side=TOP, anchor=NW, padx=20)


fm = Frame(root)
f(fm, d)
fm.pack(side=TOP, fill=None, padx=0, pady=10)
root.mainloop()
