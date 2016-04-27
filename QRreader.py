import Adafruit_BBIO.GPIO as GPIO
import time
import requests
import json
import os

def getBinary(x):
    temp = []
    for i in range(4):
        if x % 2 == 0:
            temp.append(GPIO.LOW)
        else:
            temp.append(GPIO.HIGH)
        x /= 2
    temp.reverse()
    return temp

def send(mid, mtype, mmass):

    SOME_TIME = 2
    
    pin = ["P9_11", "P9_13"]
    num = ["P8_08", "P8_10", "P8_12", "P8_14"]

    mid = getBinary(mid)
    mtype = getBinary(mtype)
    mmass = getBinary(mmass)

    # send id (11)
    GPIO.setup(pin[0], GPIO.OUT)
    GPIO.output(pin[0], GPIO.HIGH)
    GPIO.setup(pin[1], GPIO.OUT)
    GPIO.output(pin[1], GPIO.HIGH)

    for i in range(4):
        GPIO.setup(num[i], GPIO.OUT)
        GPIO.output(num[i], mid[i])

    time.sleep(SOME_TIME)

    GPIO.cleanup()

    # send type (10)
    GPIO.setup(pin[0], GPIO.OUT)
    GPIO.output(pin[0], GPIO.HIGH)
    GPIO.setup(pin[1], GPIO.OUT)
    GPIO.output(pin[1], GPIO.LOW)

    for i in range(4):
        GPIO.setup(num[i], GPIO.OUT)
        GPIO.output(num[i], mtype[i])

    time.sleep(SOME_TIME)

    GPIO.cleanup()

    # send mass (01)
    GPIO.setup(pin[0], GPIO.OUT)
    GPIO.output(pin[0], GPIO.LOW)
    GPIO.setup(pin[1], GPIO.OUT)
    GPIO.output(pin[1], GPIO.HIGH)

    for i in range(4):
        GPIO.setup(num[i], GPIO.OUT)
        GPIO.output(num[i], mmass[i])

    time.sleep(SOME_TIME)


    GPIO.cleanup()


def readQR():
    while 1 > 0:
        os.system('streamer -f jpeg -o image.jpeg')
        filename = "image.jpeg"
        files = {'file': (filename, open('image.jpeg', 'rb'))}
        r = requests.post('http://api.qrserver.com/v1/read-qr-code/', files=files)
        if r.status_code == 200:
            t = r.text
            s = json.loads(t)
            s = s[0]['symbol'][0]['data']
            if s and s != 'None':
                s = s.split(' ')
                if len(s) == 3:
                    # send in the following way: id, type, mass
                    send(int(s[0]), int(s[1]), int(s[2]))
                    print "id, type, mass"
                    print int(s[0]), int(s[1]), int(s[2])
                    print "everything is sent"
                    break
                else:
                    print "incorrect QR code"


