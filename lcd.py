from machine import Pin, SoftI2C
from I2C_LCD import I2cLcd

# Skjárinn nota I2C tengingu til að tala við ESP
i2c = SoftI2C(scl=Pin(13), sda=Pin(14), freq=400000)
# print(i2c.scan()) # sýnir addressurnar á skjáunum sem eru tengdir við 13 og 14
lcd = I2cLcd(i2c, 0x3f, 2, 16)
# EÐA ef þú færð villu á línuna hér fyrir ofan
# lcd = I2cLcd(i2c, 39, 2, 16)

# Færi bendilinn í staf nr. 0 og línu nr. 0
lcd.move_to(0, 0)
lcd.putstr("Hallo")
# Færi bendilinn í staf nr. 0 og línu nr. 1
lcd.move_to(0, 1)
lcd.putstr("Heimur")

# Skoðaðu skrána LCD_API.py til að kynna þér önnur föll sem 
# hægt er að nota með LCD skjánum