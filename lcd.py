from machine import Pin, SoftI2C
from I2C_LCD import I2cLcd
from time import sleep_ms
import random

i2c1 = SoftI2C(scl=Pin(5), sda=Pin(4), freq=400000)
lcd1 = I2cLcd(i2c1, 0x27, 2, 16)

i2c2 = SoftI2C(scl=Pin(7), sda=Pin(6), freq=400000)
lcd2 = I2cLcd(i2c2, 0x27, 2, 16)

resettakki = Pin(19, Pin.IN, Pin.PULL_UP)

takki1 = Pin(15, Pin.IN, Pin.PULL_UP)
led1= Pin(16, Pin.OUT)
takki2 = Pin(17, Pin.IN, Pin.PULL_UP)
led2 = Pin(18, Pin.OUT)
takki3 = Pin(8, Pin.IN, Pin.PULL_UP)
led3 = Pin(3, Pin.OUT)
takki4 = Pin(9, Pin.IN, Pin.PULL_UP)
led4 = Pin(10, Pin.OUT)

takki5 = Pin(39, Pin.IN, Pin.PULL_UP)
led5 = Pin(42, Pin.OUT)
takki6 = Pin(38, Pin.IN, Pin.PULL_UP)
led6 = Pin(41, Pin.OUT)
takki7 = Pin(35, Pin.IN, Pin.PULL_UP)
led7 = Pin(37, Pin.OUT)
takki8 = Pin(20, Pin.IN, Pin.PULL_UP)
led8 = Pin(45, Pin.OUT)

#ljós default off
led1.value(0)
led2.value(0)
led3.value(0)
led4.value(0)
led5.value(0)
led6.value(0)
led7.value(0)
led8.value(0)


"""
ljoskveikt = False
while True:
    print("---------")
    print(takki1.value(),"takki1")
    print(takki2.value(),"takki2")
    print(takki3.value(),"takki3")
    print(takki4.value(),"takki4")
    print("")
    print(takki5.value(),"takki5")
    print(takki6.value(),"takki6")
    print(takki7.value(),"takki7")
    print(takki8.value(),"takki8")
    print("")
    print(resettakki.value(),"reset takki")
    

    
    ljoskveikt = not ljoskveikt
    
    led1.value(ljoskveikt)
    led2.value(ljoskveikt)
    led3.value(ljoskveikt)
    led4.value(ljoskveikt)
    
    led5.value(ljoskveikt)
    led6.value(ljoskveikt)
    led7.value(ljoskveikt)
    led8.value(ljoskveikt)
    sleep_ms(100)

"""


timerstartms = 99
timerstartsec = 14
timebil = 500

#temporary
umferd = 1

timer1ms = timerstartms
timer1sec = timerstartsec
timer2ms = timerstartms
timer2sec = timerstartsec




lcd1.clear()
lcd2.clear()
lcd1.move_to(4,0)
lcd2.move_to(4,0)


while True:
    takki1_stada = takki1.value()
    takki2_stada = takki2.value()
    takki3_stada = takki3.value()
    takki4_stada = takki4.value()
    takki5_stada = takki5.value()
    takki6_stada = takki6.value()
    takki7_stada = takki7.value()
    takki8_stada = takki8.value()
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
        if takki1_stada == 0:
            umferd = 2
            sleep_ms(timebil)
        else:
            timer1ms = timer1ms - 1
            
    else:
        if umferd == 2:
            if takki2_stada == 0:
                umferd = 1
                sleep_ms(timebil)
            else:
                timer2ms = timer2ms - 1
        