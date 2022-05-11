#!/usr/bin/env python3
# -*- coding: utf-8

from tkinter import *


"""
Создайте на холсте изображение дома с травой и солнцем.
"""


if __name__ == '__main__':
    root = Tk()
    root.title('Рисунок')
    root.geometry("300x200")

    c = Canvas(root, width=200, height=200, bg='#FFFFFF')
    c.pack()

    c.create_rectangle(50, 90, 140, 175,
                       fill='#FF7F50', outline='#FF7F50')
    c.create_polygon(30, 90, 160, 90, 95, 40,
                     fill='#DEB887', outline='#DEB887')
    c.create_oval(150, 10, 190, 50,
                  fill='#FFD700', outline='#FFD700')
    x = 0
    while x < 300:
        c.create_arc(x, 160, x + 40, 250, start=200, extent=-80, style=ARC, width=2, outline='#00FF00')
        x += 15

    root.mainloop()