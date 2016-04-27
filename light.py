import Adafruit_BBIO.GPIO as GPIO

def send(id, type, mass):
    
    # send id (11)
    GPIO.setup("P9_11", GPIO.OUT)
    GPIO.output("P9_11", GPIO.HIGH)
    GPIO.setup("P9_13", GPIO.OUT)
    GPIO.output("P9_13", GPIO.HIGH)
   
    GPIO.setup("P8_08", GPIO.OUT)
    GPIO.output("P8_08", id[0])
 

GPIO.setup("P9_11", GPIO.OUT)
GPIO.output("P9_11", GPIO.HIGH)

#GPIO.cleanup()


