from machine import Pin, SoftI2C, PWM
from I2C_LCD import I2cLcd
from time import sleep_ms
import random


i2c2 = SoftI2C(scl=Pin(2), sda=Pin(42), freq=400000)
lcd2 = I2cLcd(i2c2, 39, 2, 16)



i2c1 = SoftI2C(scl=Pin(10), sda=Pin(9), freq=400000)
lcd1 = I2cLcd(i2c1, 39, 2, 16)



resettakki = Pin(40, Pin.IN, Pin.PULL_UP)

takki1 = Pin(47, Pin.IN, Pin.PULL_UP)
led1= Pin(21, Pin.OUT)
takki2 = Pin(35, Pin.IN, Pin.PULL_UP)
led2 = Pin(48, Pin.OUT)

takki3 = Pin(5, Pin.IN, Pin.PULL_UP)
led3 = Pin(4, Pin.OUT)
takki4 = Pin(7, Pin.IN, Pin.PULL_UP)
led4 = Pin(6, Pin.OUT)

takki5 = Pin(37, Pin.IN, Pin.PULL_UP)
led5 = Pin(36, Pin.OUT)
takki6 = Pin(39, Pin.IN, Pin.PULL_UP)
led6 = Pin(38, Pin.OUT)

takki7 = Pin(16, Pin.IN, Pin.PULL_UP)
led7 = Pin(15, Pin.OUT)
takki8 = Pin(18, Pin.IN, Pin.PULL_UP)
led8 = Pin(17, Pin.OUT)


#ljós default off
led1.value(0)
led2.value(0)
led3.value(0)
led4.value(0)
led5.value(0)
led6.value(0)
led7.value(0)
led8.value(0)

#NÓTUR
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
    sleep_ms(50)
    led2.value(ljoskveikt)
    sleep_ms(50)
    led3.value(ljoskveikt)
    sleep_ms(50)
    led4.value(ljoskveikt)
    sleep_ms(50)
    
    led5.value(ljoskveikt)
    sleep_ms(50)
    led6.value(ljoskveikt)
    sleep_ms(50)
    led7.value(ljoskveikt)
    sleep_ms(50)
    led8.value(ljoskveikt)
    sleep_ms(50)
    
    lcd1.move_to(8,0)
    lcd1.putstr("1")
    lcd2.move_to(8,0)
    lcd2.putstr("2")

"""
  

timerstartms = 99
timerstartsec = 14
timebil = 200
punish = 2
umferd = random.randint(1,2)

timer1ms = timerstartms
timer1sec = timerstartsec
timer2ms = timerstartms
timer2sec = timerstartsec
resettakki_stada = resettakki.value()

lcd1.clear()
lcd2.clear()
lcd1.move_to(4,0)
lcd2.move_to(4,0)


#velur hvaða takkar eru með hvaða hljóð
#i.e [4,1,3,2]
#takki 1 er hæðstur, takki 2 er lægstur, takki 3 er næst hæðstur og takki 4 er næst minnstur
takkarhljod = []
takkival = 0
count = 4
while count != 0:
    takkarrand = random.randint(1,4)
    if takkarrand in takkarhljod:
        pass
    else:
        takkarhljod.append(takkarrand)
        count = count - 1

umferdigangi = False

while True:
    takki1_stada = takki1.value()
    takki2_stada = takki2.value()
    takki3_stada = takki3.value()
    takki4_stada = takki4.value()
    takki5_stada = takki5.value()
    takki6_stada = takki6.value()
    takki7_stada = takki7.value()
    takki8_stada = takki8.value()
    if resettakki_stada == 0:
        #end condition
        umferdigangi = False
        timer1sec = timerstartsec
        timer2sec = timerstartsec
        timer1ms = timerstartms
        timer2ms = timerstartms
        umferd = random.randint(1,2)
        count = 4
        takkarhljod.clear()
        while resettakki_stada == 0:
            sleep_ms(10)
            resettakki_stada = resettakki.value()
        while count != 0:
            takkarrand = random.randint(1,4)
            if takkarrand in takkarhljod:
                pass
            else:
                takkarhljod.append(takkarrand)
                count = count - 1
        lcd1.clear()
        lcd2.clear()
        
    
    if timer1ms < 0:
        timer1ms = 99
        timer1sec = timer1sec - 1
    if timer1sec < 0:
        lcd1.clear()
        led1.value(0)
        led2.value(0)
        led3.value(0)
        led4.value(0)
        led5.value(0)
        led6.value(0)
        led7.value(0)
        led8.value(0)

        while resettakki_stada != 0:
            timer1sec = 0
            timer1ms = 0
            lcd1.move_to(8,0)
            lcd1.putstr("00")
            lcd1.move_to(7,0)
            lcd1.putstr(".")
            lcd1.move_to(6,0)
            lcd1.putstr("0")
            sleep_ms(5)
            resettakki_stada = resettakki.value()
    if timer2ms < 0:
        timer2ms = 99
        timer2sec = timer2sec - 1
    if timer2sec < 0:
        timer2sec = 0
        timer2ms = 0
        lcd2.clear()
        led1.value(0)
        led2.value(0)
        led3.value(0)
        led4.value(0)
        led5.value(0)
        led6.value(0)
        led7.value(0)
        led8.value(0)
        while resettakki_stada != 0:
            lcd2.move_to(8,0)
            lcd2.putstr("00")
            lcd2.move_to(7,0)
            lcd2.putstr(".")
            lcd2.move_to(6,0)
            lcd2.putstr("0")
            sleep_ms(5)
            resettakki_stada = resettakki.value()
    resettakki_stada = resettakki.value()
    
    lcd1.move_to(8,0)
    if timer1ms < 10:
        lcd1.putstr("0")
        lcd1.move_to(9,0)
        lcd1.putstr(str(timer1ms))
    else:
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
    if timer2ms < 10:
        lcd2.putstr("0")
        lcd2.move_to(9,0)
        lcd2.putstr(str(timer2ms))
    else:
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
    
    if umferdigangi == False:
        led1.value(0)
        led2.value(0)
        led3.value(0)
        led4.value(0)
        led5.value(0)
        led6.value(0)
        led7.value(0)
        led8.value(0)
    
    takkarumferd = 0
    if umferd == 1 and umferdigangi == False:
        takkival = random.randint(0,3)
        takkarumferd = takkarhljod[takkival]
        led1.value(0)
        led2.value(0)
        led3.value(0)
        led4.value(0)
        led5.value(0)
        led6.value(0)
        led7.value(0)
        led8.value(0)
        sleep_ms(timebil)
        
        lcd1.clear()
        if takkival == 0:
            led1.value(1)
        if takkival == 1:
            led2.value(1)
        if takkival == 2:
            led3.value(1)
        if takkival == 3:
            led4.value(1)
        else:
            pass
        
        print(takkival)
        umferdigangi = True
        
    else:
        if umferd == 2 and umferdigangi == False:
            takkival = random.randint(0,3)
            takkarumferd = takkarhljod[takkival]
            sleep_ms(timebil)
            lcd2.clear()
            sleep_ms(timebil)
            

            if takkival == 0:
                led5.value(1)
            if takkival == 1:
                led6.value(1)
            if takkival == 2:
                led7.value(1)
            if takkival == 3:
                led8.value(1)
            else:
                pass
        
            print(takkival)
            umferdigangi = True

        
    if umferd == 1 and umferdigangi == True:
        if takki1_stada == 0:
            if takkival == 0:
                umferd = 2
                umferdigangi = False
            if takkival == 1:
                umferd = 2
                umferdigangi = False
                timer1sec = timer1sec - punish
            if takkival == 2:
                umferd = 2
                umferdigangi = False
                timer1sec = timer1sec - punish
            if takkival == 3:
                umferd = 2
                umferdigangi = False
                timer1sec = timer1sec - punish
                
        if takki2_stada == 0:
            if takkival == 0:
                umferd = 2
                umferdigangi = False
                timer1sec = timer1sec - punish
            if takkival == 1:
                umferd = 2
                umferdigangi = False
            if takkival == 2:
                umferd = 2
                umferdigangi = False
                timer1sec = timer1sec - punish
            if takkival == 3:
                umferd = 2
                umferdigangi = False
                timer1sec = timer1sec - punish
                
        if takki3_stada == 0:
            if takkival == 0:
                umferd = 2
                umferdigangi = False
                timer1sec = timer1sec - punish
            if takkival == 1:
                umferd = 2
                umferdigangi = False
                timer1sec = timer1sec - punish
            if takkival == 2:
                umferd = 2
                umferdigangi = False
            if takkival == 3:
                umferd = 2
                umferdigangi = False
                timer1sec = timer1sec - punish
                
        if takki4_stada == 0:
            if takkival == 0:
                umferd = 2
                umferdigangi = False
                timer1sec = timer1sec - punish
            if takkival == 1:
                umferd = 2
                umferdigangi = False
                timer1sec = timer1sec - punish
            if takkival == 2:
                umferd = 2
                umferdigangi = False
                timer1sec = timer1sec - punish
            if takkival == 3:
                umferd = 2
                umferdigangi = False

        
        timer1ms = timer1ms - 1
    else:

        if umferd == 2 and umferdigangi == True:
            if takki5_stada == 0:
                if takkival == 0:
                    umferd = 1
                    umferdigangi = False
                if takkival == 1:
                    umferd = 1
                    umferdigangi = False
                    timer2sec = timer2sec - punish
                if takkival == 2:
                    umferd = 1
                    umferdigangi = False
                    timer2sec = timer2sec - punish
                if takkival == 3:
                    umferd = 1
                    umferdigangi = False
                    timer2sec = timer2sec - punish
                    
            if takki6_stada == 0:
                if takkival == 0:
                    umferd = 1
                    umferdigangi = False
                    timer2sec = timer2sec - punish
                if takkival == 1:
                    umferd = 1
                    umferdigangi = False
                if takkival == 2:
                    umferd = 1
                    umferdigangi = False
                    timer2sec = timer2sec - punish
                if takkival == 3:
                    umferd = 1
                    umferdigangi = False
                    timer2sec = timer2sec - punish
                
            if takki7_stada == 0:
                if takkival == 0:
                    umferd = 1
                    umferdigangi = False
                    timer2sec = timer2sec - punish
                if takkival == 1:
                    umferd = 1
                    umferdigangi = False
                    timer2sec = timer2sec - punish
                if takkival == 2:
                    umferd = 1
                    umferdigangi = False
                if takkival == 3:
                    umferd = 1
                    umferdigangi = False
                    timer2sec = timer2sec - punish
                
            if takki8_stada == 0:
                if takkival == 0:
                    umferd = 1
                    umferdigangi = False
                    timer2sec = timer2sec - punish
                if takkival == 1:
                    umferd = 1
                    umferdigangi = False
                    timer2sec = timer2sec - punish
                if takkival == 2:
                    umferd = 1
                    umferdigangi = False
                    timer2sec = timer2sec - punish
                if takkival == 3:
                    umferd = 1
                    umferdigangi = False

        
            timer2ms = timer2ms - 1
            
            
    sleep_ms(5)
               
    
    



