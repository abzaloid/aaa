import Adafruit_BBIO.GPIO as GPIO

def getBinary(x):
	temp = []
	for i in range(4):
		temp.append(x % 2)
		x /= 2
	temp.reverse()
	return temp

def send(mid, mtype, mmass):
    
	pin = ["P9_11", "P9_13"]
	nums = ["P8_08", "P8_10", "P8_12", "P8_14"]

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

	GPIO.cleanup()

    # send type (10)
    GPIO.setup(pin[0], GPIO.OUT)
    GPIO.output(pin[0], GPIO.HIGH)
    GPIO.setup(pin[1], GPIO.OUT)
    GPIO.output(pin[1], GPIO.LOW)

	for i in range(4):
	    GPIO.setup(num[i], GPIO.OUT)
	    GPIO.output(num[i], mtype[i])

	GPIO.cleanup()

    # send mass (01)
    GPIO.setup(pin[0], GPIO.OUT)
    GPIO.output(pin[0], GPIO.LOW)
    GPIO.setup(pin[1], GPIO.OUT)
    GPIO.output(pin[1], GPIO.HIGH)

	for i in range(4):
	    GPIO.setup(num[i], GPIO.OUT)
	    GPIO.output(num[i], mmass[i])

	GPIO.cleanup()



#GPIO.cleanup()
