from microbit import *
from random import randint
d = 20

def roll():
    r = randint(1, d)
    display.scroll(r)

def advantage():
    r1 = randint(1, d)
    r2 = randint(1, d)
    if r1 > r2:
        display.scroll(r1)
    else:
        display.scroll(r2)

def disadvantage():
    r1 = randint(1, d)
    r2 = randint(1, d)
    if r1 < r2:
       display.scroll(r1)
    else:
        display.scroll(r2)
        
while True:
    if button_a.is_pressed() and accelerometer.was_gesture("shake"):
        advantage()
    elif button_b.is_pressed() and accelerometer.was_gesture("shake"):
        disadvantage()
    elif accelerometer.was_gesture("shake"):
        roll()
    elif button_a.is_pressed() and button_b.is_pressed():
        break
    