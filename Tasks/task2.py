#!/usr/bin/env python3
# -*- coding: utf-8

from tkinter import *


"""
Напишите программу по следующему описанию. Нажатие Enter в однострочном текстовом 
поле приводит к перемещению текста из него в список (экземпляр Listbox ). При двойном 
клике ( <Double-Button-1> ) по элементу-строке списка, она должна копироваться в текстовое поле.
"""


def add_item(event):
    name = ent.get()
    lbox.insert(0, name)
    ent.delete(0, 'end')


def copy_item(event):
    product = []
    select = list(lbox.curselection())
    select.reverse()
    for item in select:
        p = lbox.get(item)
        product.append(p)
    for v in product:
        ent.insert(0, v)
    for k in select:
        lbox.delete(k)


if __name__ == '__main__':
    root = Tk()
    root.title('Перемещение текста')
    root.geometry('200x180')

    ent = Entry(root, width=20, font=36)

    lbox = Listbox(width=30)

    ent.grid(row=1, column=1)
    lbox.grid(row=2, column=1, pady=5)

    ent.bind('<Return>', add_item)
    lbox.bind('<Double-Button-1>', copy_item)

    root.mainloop()