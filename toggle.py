#use the pin method from the machine software library 
from machine import Pin 
import time  # gives time for the bouncing to settle so the microcontroller only reads the appropriate amount of bounces , debounces

led = Pin(16, Pin.OUT)
button = Pin(22, Pin.IN, Pin.PULL_DOWN)

led_state = False    #Tracking Led Status, false means led is CURRENTLY off
prev_button = 0      #Stores previous buttons "status", 0 means button was not pressed last check

while True: 
    curr_button = button.value()     # reads current state of the button (1 = pressed, 0 = not pressed)

    if curr_button == 1 and prev_button == 0:  #check for new button press
        time.sleep_ms(20) #debounce, delaying to avoid false triggers

        if button.value() == 1:  #confirm button is still pressed after debounce
            led_state = not led_state   #toggle led state
            led.value(led_state)   #update the led light

            while button.value() == 1: #wait until button is released
                time.sleep_ms(10)
    
    prev_button = curr_button #remember current button state for next loop