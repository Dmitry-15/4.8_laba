#!/usr/bin/env python3
# -*- coding: utf-8

from tkinter import Tk, Canvas, ARC


"""
Создайте на холсте изображение дома с травой и солнцем.
"""


if __name__ == '__main__':
    root = Tk()
    root.title('Рисунок')
    root.geometry("500x400")

    c = Canvas(root, width=500, height=400, bg='#FFFFFF')
    c.pack()

    c.create_oval(383, 18, 450, 84, fill="#FFD700")
    c.create_rectangle(129, 143, 340, 360, fill='#FF6347')
    c.create_rectangle(164, 166, 301, 215, fill='#14FCF8')
    c.create_rectangle(226, 165, 236, 215, fill='#FFDAB9')
    c.create_rectangle(198, 282, 248, 360, fill='#FFDAB9')
    c.create_polygon(232, 30, 90, 144, 375, 143, fill='#804040')
    c.create_oval(232, 318, 240, 328, fill="#400000")

    x = 0
    while x < 500:
        c.create_arc(x, 455, x + 40, 355, start=150, extent=-80, style=ARC, width=3, outline='#00FF7F')
        x += 15

    root.mainloop()