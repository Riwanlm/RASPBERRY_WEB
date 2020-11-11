#import des utilistaires python
import RPi.GPIO as GPIO
import time

class Led:
    def __init__(self, numGPIO):
        self.shouldCancel = False
        # constructeur pour instancier notre objet Led
        # creation d'une variable d'instance "Numero de GPIO"
        self.numGPIO = numGPIO
        # On dit au raspberry qu'on utilise la broche pour "ecrire" dessus en mode "sortie"
        GPIO.setup(self.numGPIO, GPIO.OUT)
    
    # method "on" pour allumer la led
    def on(self):
        print('Led '+str(self.numGPIO)+' on')
        # On dit a la broche d'envoyer du courant
        GPIO.output(self.numGPIO, GPIO.HIGH)

    # method "off" pour eteindre la led
    def off(self):
        print('Led '+str(self.numGPIO)+' off')
        # on dit a la broche d'arreter d'envoyer du courant
        GPIO.output(self.numGPIO, GPIO.LOW)

    def cancel(self):
        self.shouldCancel = True

    def blink(self, numBlink, sleepTime):
        i = 0
        self.shouldCancel = False
        while i < numBlink and not self.shouldCancel:
            self.on()
            time.sleep(sleepTime)
            self.off()
            time.sleep(sleepTime)
            i += 1