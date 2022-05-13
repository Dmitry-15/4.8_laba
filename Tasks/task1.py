#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import Tk, Button, Listbox, EXTENDED, END


"""
Напишите программу, состоящую из двух списков Listbox . В первом будет,
например, перечень товаров, заданный программно. Второй изначально пуст, пусть это
будет перечень покупок. При клике на одну кнопку товар должен переходить из одного
списка в другой. При клике на вторую кнопку – возвращаться (человек передумал покупать).
Предусмотрите возможность множественного выбора элементов списка и их перемещения.
"""


def add_item():
    product = []
    select = list(lbox_right.curselection())
    select.reverse()
    for item in select:
        p = lbox_right.get(item)
        product.append(p)
    for v in product:
        lbox_left.insert(0, v)
    for k in select:
        lbox_right.delete(k)


def del_item():
    product = []
    select = list(lbox_left.curselection())
    select.reverse()
    for item in select:
        p = lbox_left.get(item)
        product.append(p)
    for v in product:
        lbox_right.insert(0, v)
    for k in select:
        lbox_left.delete(k)


if __name__ == '__main__':
    root = Tk()
    root.title('Список продуктов')
    root.geometry('366x188')

    products = ['apple', 'bananas', 'carrot', 'bread', 'butter', 'meat', 'milk', 'tomato', 'potato', 'pineapple']

    lbox_right = Listbox(selectmode=EXTENDED)
    lbox_left = Listbox(selectmode=EXTENDED)

    button_right = Button(height=1, width=5, text='>>>>', command=add_item)
    button_left = Button(height=1, width=5, text='<<<<', command=del_item)

    lbox_right.grid(row=1, column=1, pady=15, padx=3)
    lbox_left.grid(row=1, column=4, pady=15)

    button_right.grid(row=1, column=2, padx=3)
    button_left.grid(row=1, column=3, padx=5)

    for i in products:
        lbox_right.insert(END, i)

    root.mainloop()
