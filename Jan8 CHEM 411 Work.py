from time import sleep_ms
from machine import Pin

#setup
led=Pin(12,Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_UP)

while True:
    if button.value() == 0:
        led.value(1)
    else:
        led.value(0)
        sleep_ms(100)
    
    #led.value(1) 
    #sleep_ms(500)
    #led.value(0)
    #sleep_ms(100)
        
        #elapsed = time.time() for A1, for timing

#utime for microcontroller