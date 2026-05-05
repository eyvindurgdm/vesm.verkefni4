from machine import Pin, SoftI2C
from I2C_LCD import I2cLcd
from time import sleep_ms

# Skjárinn nota I2C tengingu til að tala við ESP
i2c = SoftI2C(scl=Pin(13), sda=Pin(14), freq=400000)
# print(i2c.scan()) # sýnir addressurnar á skjáunum sem eru tengdir við 13 og 14
# lcd = I2cLcd(i2c, 0x3f, 2, 16)
# EÐA ef þú færð villu á línuna hér fyrir ofan
lcd = I2cLcd(i2c, 39, 2, 16)


# Skoðaðu skrána LCD_API.py til að kynna þér önnur föll sem 
# hægt er að nota með LCD skjánum
timerms = 99
timersec = 14
lcd.move_to(4,0)

while True:
    if timerms < 0:
        timerms = 99
        timersec = timersec - 1
    if timersec < 0:
        #end condition
        timersec = 40
        lcd.clear()
        sleep_ms(1000)
    lcd.move_to(7,0)
    lcd.putstr(str(timerms))
    lcd.move_to(6,0)
    lcd.putstr(".")
    if timersec == 9 and timerms == 99:
        lcd.clear()
    if timersec < 10:
        lcd.move_to(5,0)
    else:
        lcd.move_to(4,0)
    lcd.putstr(str(timersec))
    timerms = timerms - 1
    sleep_ms(5)