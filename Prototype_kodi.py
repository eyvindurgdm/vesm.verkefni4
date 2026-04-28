from machine import Pin, PWM
import time
import random


takkar = [
    Pin(1, Pin.IN),   
    Pin(2, Pin.IN), 
    Pin(3, Pin.IN), 
    Pin(4, Pin.IN),   
    Pin(5, Pin.IN),
    Pin(6, Pin.IN),
    Pin(7, Pin.IN),
    Pin(8, Pin.IN)
]


led = [
    Pin(9, Pin.OUT),
    Pin(10, Pin.OUT),
    Pin(11, Pin.OUT),
    Pin(12, Pin.OUT),
    Pin(13, Pin.OUT),
    Pin(14, Pin.OUT),
    Pin(15, Pin.OUT),
    Pin(16, Pin.OUT)
]

#BUZZER

buzzer = PWM(Pin(20))
buzzer.duty(0)  # byrja slokktur

#NÓTUR

C4 = 262
E4 = 330
G4 = 392
A4 = 440

C5 = 523
E5 = 659
G5 = 784

G3 = 196
C3 = 131

#GRUNN HLJÓÐ

def pip(tidni, lengd):
    # stilla hz
    buzzer.freq(tidni)
    
    # kveikja a buzzer
    buzzer.duty(512)
    
    # biða a meðan hljóð spilar
    time.sleep(lengd)
    
    # slökkva aftur
    buzzer.duty(0)

#HLJÓÐ FYRIR TAKKA
def spila_hljod(numer):
    # hver takki hefur sitt hljod
    tonar = [C4, E4, G4, A4]
    
    # spila tón
    pip(tonar[numer], 0.3)

# SIGUR HLJÓÐ (rett svar)

def sigur_hljod():
    pip(C5, 0.1)
    time.sleep(0.05)
    pip(E5, 0.1)
    time.sleep(0.05)
    pip(G5, 0.2)


# TAP HLJÓ' (rangt svar)

def tap_hljod():
    pip(G3, 0.2)
    time.sleep(0.05)
    pip(C3, 0.3)

# SÝNA TAKKA (kennsla)

def syna_takka(vorpun):
    # fara í gegnum alla 4 takka
    for i in range(4):
        
        # kveikja á LED
        led[i].on()
        
        # spila hljð sem tengist takkanum
        spila_hljod(vorpun[i])
        
        # smæa bið svo notandi sjá
        time.sleep(0.3)
        
        # slökkva æ LED
        led[i].off()
        
        time.sleep(0.2)

# BIÐA EFTIR AÐ ÝTT SÉ Á TAKKA

def bida_efter_takka():
    while True:
        for i in range(4):
            if takkar[i].value() == 1:
                return i  # skilar hvaða takki var yttur

# UMFERD

def spila_umferd(kennsla):

    # random mapping milli takka og hljóð
    vorpun = [0,1,2,3]
    random.shuffle(vorpun)

    if kennsla:
        syna_takka(vorpun)  # sýna ljós + hljóð
        time.sleep(1)

    # taka tima
    byrjun = time.ticks_ms()
    
    refs = 0  # refsýng

    while True:
        # velja random hljóð sem leikmaðr a að finna
        mark = random.randint(0,3)

        # spila hljóð
        spila_hljod(mark)

        # biða eftir input
        val = bida_efter_takka()

        # athuga hvort rettur takki var yttur
        if vorpun[val] == mark:
            sigur_hljod()
            break  # fer út úr while (umferð klára)
        else:
            tap_hljod()
            refs += 2000  # +2 sek refsýng

    # taka enda týma
    endir = time.ticks_ms()

    # reikna heildartíma + refs
    heild = time.ticks_diff(endir, byrjun) + refs

    return heild

# AðAAl LEIKUR

def leikur(ö):

    timar = [0,0]  # geymir tima fyrir 2 leikmenn

    for leikmadur in range(2):

        summa = 0

        # 4 umferðir per leikmann
        for umferd in range(4):

            # fyrstu 2 = kennsla (með ljós)
            if umferd < 2:
                kennsla = True
            else:
                kennsla = False

            t = spila_umferd(kennsla)
            summa += t

            # smá pása milli umferða
            time.sleep(1)

        timar[leikmadur] = summa

    # SIGURVEGARI

    if timar[0] < timar[1]:
        # leikmadur 1 vann. 2x sigur hljod
        sigur_hljod()
        time.sleep(0.2)
        sigur_hljod()
    else:
        # leikmadur 2 vann. 2x tap hljod
        tap_hljod()
        time.sleep(0.2)
        tap_hljod()

leikur()
