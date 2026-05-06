from machine import Pin, SoftI2C
from I2C_LCD import I2cLcd
from time import sleep_ms
import random

i2c1 = SoftI2C(scl=Pin(13), sda=Pin(14), freq=400000)
lcd1 = I2cLcd(i2c1, 39, 2, 16)

i2c2 = SoftI2C(scl=Pin(5), sda=Pin(4), freq=400000)
lcd2 = I2cLcd(i2c2, 0x27, 2, 16)

takki1 = Pin(15, Pin.IN, Pin.PULL_UP)
takki2 = Pin(18, Pin.IN, Pin.PULL_UP)
resettakki = Pin(19, Pin.IN, Pin.PULL_UP)
punish = Pin(10, Pin.IN, Pin.PULL_UP)

timerstartms = 99
timerstartsec = 14
timer1ms = timerstartms
timer1sec = timerstartsec
timer2ms = timerstartms
timer2sec = timerstartsec
umferd = random.randint(1,2)
timebil = 500

lcd1.clear()
lcd2.clear()
lcd1.move_to(4,0)
lcd2.move_to(4,0)


while True:
    takki1_stada = takki1.value()
    takki2_stada = takki2.value()
    resettakki_stada = resettakki.value()
    if timer1ms < 0:
        timer1ms = 99
        timer1sec = timer1sec - 1
    if timer1sec < 0 or resettakki.value() == 0:
        #end condition
        timer1sec = timerstartsec
        timer2sec = timerstartsec
        timer1ms = timerstartms
        timer2ms = timerstartms
        lcd1.clear()
        lcd2.clear()
        sleep_ms(1000)
        umferd = random.randint(1,2)
        
    if timer2ms < 0:
        timer2ms = 99
        timer2sec = timer2sec - 1
    if timer2sec < 0:
        timer1sec = timerstartsec
        timer2sec = timerstartsec
        timer1ms = timerstartms
        timer2ms = timerstartms
        lcd1.clear()
        lcd2.clear()
        sleep_ms(1000)
        umferd = random.randint(1,2)
        

    
    lcd1.move_to(8,0)
    lcd1.putstr(str(timer1ms))
    lcd1.move_to(7,0)
    lcd1.putstr(".")
    if timer1sec < 10 and timer1ms == 99:
        lcd1.clear()
    if timer1sec < 10:
        lcd1.move_to(6,0)
    else:
        lcd1.move_to(5,0)
    lcd1.putstr(str(timer1sec))
    
    
    lcd2.move_to(8,0)
    lcd2.putstr(str(timer2ms))
    lcd2.move_to(7,0)
    lcd2.putstr(".")
    if timer2sec < 10 and timer2ms == 99:
        lcd2.clear()
    if timer2sec < 10:
        lcd2.move_to(6,0)
    else:
        lcd2.move_to(5,0)
    lcd2.putstr(str(timer2sec))
    
    
    
    if umferd == 1:
        if punish.value() == 0:
            timer1sec = timer1sec - 2
            while punish.value() == 0:
                sleep_ms(10)
            umferd = 2
            lcd1.clear()
        else:
            if takki1_stada == 0:
                umferd = 2
                sleep_ms(timebil)
            else:
                timer1ms = timer1ms - 1
            
    else:
        if umferd == 2:
            if punish.value() == 0:
                timer2sec = timer2sec - 2
                while punish.value() == 0:
                    sleep_ms(10)
                umferd = 1
                lcd2.clear()
            else: 
                if takki2_stada == 0:
                    umferd = 1
                    sleep_ms(timebil)
                else:
                    timer2ms = timer2ms - 1
    
    sleep_ms(5)