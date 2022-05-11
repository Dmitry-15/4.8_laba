#!/usr/bin/env python3
# -*- coding: utf-8

from tkinter import *


"""
B программе создается анимация круга, который движется от левой границы холста до правой. 
Изучите приведенную программу и самостоятельно запрограммируйте постепенное движение фигуры 
в ту точку холста, где пользователь кликает левой кнопкой мыши. Координаты события хранятся 
в его атрибутах x и y (event.x, event.y).
"""


def click(event):
    c.x = event.x + c.radius
    c.y = event.y + c.radius
    motion()


def motion():
    x = c.coords(c.ball)[2]
    y = c.coords(c.ball)[3]
    if c.x == x and c.y == y:
        return
    if c.x < x:
        c.move(c.ball, -1, 0)
    if c.x > x:
        c.move(c.ball, 1, 0)
    if c.y < y:
        c.move(c.ball, 0, -1)
    if c.y > y:
        c.move(c.ball, 0, 1)
    root.after(10, motion)


if __name__ == "__main__":
    root = Tk()
    root.title('Движение объекта')
    root.geometry("500x300")

    c = Canvas(root, width=500, height=300, bg="white")

    c.pack()
    c.radius = 30
    c.ball = c.create_oval(0, 150, c.radius * 3, 150 + c.radius * 3, fill='#9400D3')

    c.bind("<Button-1>", click)

    root.mainloop()