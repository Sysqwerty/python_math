# !/usr/bin/python3
from tkinter import *
root = Tk()

c = Canvas(root, width=340, height=240, bg='white')  # Розмір та колір
c.pack()


def set1(x, y):
    out = 0
    if (x-120)**2+(y-120)**2 <= 10000:
        out = 1
    return out


def border1(x, y):
    out = 0
    if 9600 <= (x-120)**2+(y-120)**2 <= 10000:
        out = 1
    return out


def set2(x, y):
    out = 0
    if (x-220)**2+(y-120)**2 <= 10000:
        out = 1
    return out


def border2(x, y):
    out = 0
    if 9600 <= (x-220)**2+(y-120)**2 <= 10000:
        out = 1
    return out


def border():
    for x in range(400):
        for y in range(400):
            if border1(x, y) or border2(x, y):
                c.create_line(x, y, x, y+1, fill='black')
