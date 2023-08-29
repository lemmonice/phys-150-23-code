import board
import digitalio
import time
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT
while True:
    for brightness in [.8, .2]:
        T_fast = 0.01
        T_on = brightness*T_fast
        T_off = (1-brightness)*T_fast
    # note the new line: "a" is a variable that takes the values that are
        # listed in square brackets.  This loop is sometimes called a "foreach"
        num_repeats = 100
        i = 0
        while (i < num_repeats):
            led.value = True
            time.sleep(T_on)
            led.value = False
            time.sleep(T_off)
            i = i+1
