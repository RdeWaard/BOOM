from microbit import *
#dicebag

dicebag = [2, 4, 6, 8, 10, 12, 20, 100]
i = 0
p = 0
while True:
    if button_b.is_pressed():
        i = i + 1
        p = i%8
        #display.show(i)
  #  sleep(3000)
        type = dicebag[p]
        display.show(type)
