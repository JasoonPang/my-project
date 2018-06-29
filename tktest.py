# -*- coding: utf-8 -*-
# @Time    : 2018/6/29 14:31
# @Author  : JasoonPang
# @Email   : 724719274@qq.com

from tkinter import *
from tkinter import Frame

root = Tk()
root.title('故障查询')  # 标题
Label(root, text='故障查询', bg='green', width=120, height=2).pack(side=TOP)  # 整个板块名称


Fm1 = Frame(root)
# 生成第一部分的前两行示例部分
for _ in range(2):
    fm1 = Frame(Fm1)
    for _ in range(8):
        Button(fm1, text='辅导课', width=12).pack(side=LEFT, anchor=NW, padx=20)
    fm1.pack(side=TOP, fill=BOTH, padx=80,  pady=10)

# 生成第一部分的第三行
fm3 = Frame(Fm1)
Label(fm3, text='相关：', width=12).pack(side=LEFT, anchor=NW)  # 生成相关标签
for _ in range(5):
    Button(fm3, text='筛素数', width=10).pack(side=LEFT, anchor=NW, padx=10)  # 生成相关的例子部分
Entry(fm3, bg='white', width=20).pack(side=LEFT, anchor=NW, padx=25)       # 生成输入框
Button(fm3, text='查询', width=10).pack(side=LEFT, anchor=NW, padx=10)     # 生成查询按钮
fm3.pack(side=TOP, fill=None, padx=0, pady=10)

Fm1.pack(side=TOP, fill=None, padx=2, pady=5)  # 整体第一部分到此结束

Fm2 = Frame(root)  # 整体第二部分
fm4 = Frame(Fm2)
for _ in range(3):
    Button(fm4, text='筛素数', width=30).pack(side=LEFT, anchor=NW, padx=20)  # 生成三大示例类型
fm4.pack(side=TOP, fill=None, padx=0, pady=10)


d = {'汽车': {'发动机': 1, '轮胎': 2, '油缸': 3}}  # 示例索引结果格式


def f(fm, d_dict):
    """生成被索引结果，d为索引的结果列表
    :param fm: 在该模块下生成结果
    :type d_dict: 搜索结果，可更改样式
    """
    keys = list(d_dict.keys())
    for i in keys:
        for j in d_dict[i]:
            # 以下可视需求更改展示类型（按钮或标签）
            Button(fm, text='{}  {}    {}'.format(i, j, d_dict[i][j]), width=30).pack(side=TOP, anchor=NW, padx=20)


fm5 = Frame(Fm2)
# 三次循环，生成三个表
for _ in range(3):
    fm51 = Frame(fm5)
    f(fm51, d)
    fm51.pack(side=LEFT, fill=None, padx=0, pady=20)
fm5.pack(side=TOP, fill=None, padx=0, pady=10)

Fm2.pack(side=TOP, after=Fm1, fill=None, padx=2, pady=10)

root.mainloop()