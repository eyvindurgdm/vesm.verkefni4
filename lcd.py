from machine import Pin, SoftI2C
from I2C_LCD import I2cLcd
from time import sleep_ms

i2c = SoftI2C(scl=Pin(13), sda=Pin(14), freq=400000)
lcd = I2cLcd(i2c, 39, 2, 16)
takki1 = Pin(15, Pin.IN, Pin.PULL_UP)
takki2 = Pin(18, Pin.IN, Pin.PULL_UP)

timerstartms = 99
timerstartsec = 14
timer1ms = timerstartms
timer1sec = timerstartsec
timer2ms = timerstartms
timer2sec = timerstartsec
umferd = 1
lcd.move_to(4,0)


while True:
    takki1_stada = takki1.value()
    takki2_stada = takki2.value()
    print(takki1_stada)
    if timer1ms < 0:
        timer1ms = 99
        timer1sec = timer1sec - 1
    if timer1sec < 0:
        #end condition
        timer1sec = timerstartsec
        timer2sec = timerstartsec
        timer1ms = timerstartms
        timer2ms = timerstartms
        lcd.clear()
        sleep_ms(1000)    
        
    if timer2ms < 0:
        timer2ms = 99
        timer2sec = timer2sec - 1
    if timer2sec < 0:
        timer1sec = timerstartsec
        timer2sec = timerstartsec
        timer1ms = timerstartms
        timer2ms = timerstartms
        lcd.clear()
        sleep_ms(1000)  
        

        
    lcd.move_to(8,0)
    lcd.putstr(str(timer1ms))
    lcd.move_to(7,0)
    lcd.putstr(".")
    if timer1sec == 9 and timer1ms == 99:
        lcd.clear()
    if timer1sec < 10:
        lcd.move_to(6,0)
    else:
        lcd.move_to(5,0)
    lcd.putstr(str(timer1sec))
    
    lcd.move_to(8,1)
    lcd.putstr(str(timer2ms))
    lcd.move_to(7,1)
    lcd.putstr(".")
    if timer2sec == 9 and timer2ms == 99:
        lcd.clear()
    if timer2sec < 10:
        lcd.move_to(6,1)
    else:
        lcd.move_to(5,1)
    lcd.putstr(str(timer2sec))
    
    if umferd == 1:
        timer1ms = timer1ms - 1
        if takki1_stada == 0:
            umferd = 2
    if umferd == 2:
        timer2ms = timer2ms - 1
        if takki2_stada == 0:
            umferd = 1
    
    
    """if takki1_stada == 0:
        timer1ms = timer1ms - 1
    if takki2_stada == 0:
        timer2ms = timer2ms - 1"""
    
    sleep_ms(5)