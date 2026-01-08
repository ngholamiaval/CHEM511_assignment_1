from time import sleep_ms
from machine import Pin

current = time.time() #this is seconds elapsed since 1984

led=Pin(12,Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_UP)

while True:
    if button.value() == 0:
        led.value(1)
    else:
        led.value(0)
        sleep_ms(100) #this is for the delay, it doesn't need to be looking every microseconds, give it a chance to chill out
        
elapsed = time.time () - current #this is how you can 

    
    
    