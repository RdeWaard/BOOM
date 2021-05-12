from tkinter import *
from random import randint
window = Tk()
text = Text(window, width=20, height=5)

dtype = 2
mod = 0

def rollDice():
    dtype = dice_type.get()
    mod = modifier.get()
    roll = randint(1, int(dtype))
    if roll == 1 or roll == int(dtype):
        if roll == int(dtype):
            value = 'natural ', dtype, '+', mod
        else:
            value = 'natural 1 + ', mod
    else:    
        value = roll + int(mod)
    Label(window, text=value).pack()
    
dice_type = Entry(window)
modifier = Entry(window)
dice_type.pack()
modifier.pack()

Button(
    window,
    text='roll',
    command=rollDice
    ).pack()
window.mainloop()