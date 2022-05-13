#!/usr/bin/env python3
# -*- coding: utf-8

from tkinter import Tk, Button, Text, Entry, Label, CENTER


"""
Напишите программу по описанию. Размеры многострочного текстового поля определяются 
значениями, введенными в однострочные текстовые поля. Изменение размера происходит 
при нажатии мышью на кнопку, а также при нажатии клавиши Enter. Цвет фона экземпляра 
Text светлосерый ( lightgrey ), когда поле не в фокусе, и белый, когда имеет фокус.
"""


def change(event):
    a = ent1.get()
    b = ent2.get()
    txt['width'] = a
    txt['height'] = b


def button():
    a = ent1.get()
    b = ent2.get()
    txt['width'] = a
    txt['height'] = b


def focus(event):
    txt['bg'] = 'white'


def unfocus(event):
    txt['bg'] = 'lightgrey'


if __name__ == '__main__':
    root = Tk()
    root.title('Изменение размера текстового поля')
    root.geometry('360x240')

    label1 = Label(root, text="Ширина ", font=25)
    label2 = Label(root, text="Высота ", font=25)

    ent1 = Entry(root, width=10, font=36, justify=CENTER)
    ent2 = Entry(root, width=10, font=36, justify=CENTER)

    button = Button(height=1, width=8, text='Изменить', command=button)
    txt = Text(root, width=20, height=10, bg="lightgrey", font=12)

    ent1.grid(row=1, column=1)
    ent2.grid(row=2, column=1)

    label1.grid(row=1, column=0)
    label2.grid(row=2, column=0)

    button.grid(row=1, column=2, padx=10)

    txt.grid(row=3, column=0)

    button.bind('<Return>', change)
    txt.bind('<FocusIn>', focus)
    txt.bind('<FocusOut>', unfocus)

    root.mainloop()