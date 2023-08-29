# Write your code here :-)
import board
import digitalio
import time

# set up the (red) LED
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

while True:
    for brightness in [1, .9, .8, .7, .6, .5, .4, .3, .2, .1, 0, .1, .2, .3, .4, .5, .6, .7, .8, .9]:
        # brightness is measured out of a max of 1.0
        T_fast = 0.01
        T_on = brightness*T_fast
        T_off = (1-brightness)*T_fast
        num_repeats=10
        i=0
        while (i<num_repeats):
            led.value = True
            time.sleep(T_on)
            led.value = False
            time.sleep(T_off)
            i=i+1
