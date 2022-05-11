#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *


"""
Напишите программу, состоящую из двух списков Listbox . В первом будет,
например, перечень товаров, заданный программно. Второй изначально пуст, пусть это
будет перечень покупок. При клике на одну кнопку товар должен переходить из одного
списка в другой. При клике на вторую кнопку – возвращаться (человек передумал покупать).
Предусмотрите возможность множественного выбора элементов списка и их перемещения.
"""


def add_item():
    product = []
    select = list(lbox_first.curselection())
    select.reverse()
    for item in select:
        p = lbox_first.get(item)
        product.append(p)
    for v in product:
        lbox_second.insert(0, v)
    for k in select:
        lbox_first.delete(k)


def del_item():
    product = []
    select = list(lbox_second.curselection())
    select.reverse()
    for item in select:
        p = lbox_second.get(item)
        product.append(p)
    for v in product:
        lbox_first.insert(0, v)
    for k in select:
        lbox_second.delete(k)


if __name__ == '__main__':
    root = Tk()
    root.title('Список продуктов')
    root.geometry('400x200')

    products = ['apple', 'bananas', 'carrot', 'bread', 'butter', 'meat', 'milk', 'tomato', 'potato', 'pineapple']

    lbox_first = Listbox(selectmode=EXTENDED)
    lbox_second = Listbox(selectmode=EXTENDED)

    button_right = Button(height=1, width=5, text='>>>>', command=add_item)
    button_left = Button(height=1, width=5, text='<<<<', command=del_item)

    lbox_first.grid(row=1, column=1, pady=15, padx=3)
    lbox_second.grid(row=1, column=4, pady=15)

    button_right.grid(row=1, column=2, padx=3)
    button_left.grid(row=1, column=3, padx=5)

    for i in products:
        lbox_first.insert(END, i)

    root.mainloop()
