#!/usr/bin/env python

# Import required modules
import time
import RPi.GPIO as GPIO


# set up GPIO pins
def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(29, GPIO.OUT) # Connected to PWMA
    GPIO.setup(11, GPIO.OUT) # Connected to AIN2
    GPIO.setup(12, GPIO.OUT) # Connected to AIN1
    GPIO.setup(13, GPIO.OUT) # Connected to STBY
    GPIO.setup(15, GPIO.OUT) # Connected to BIN1
    GPIO.setup(16, GPIO.OUT) # Connected to BIN2
    GPIO.setup(18, GPIO.OUT) # Connected to PWMB



# Drive the motor clockwise
def forward(sec):
    
    # Motor A:
    GPIO.output(12, GPIO.HIGH) # Set AIN1
    GPIO.output(11, GPIO.LOW) # Set AIN2
    # Motor B:
    GPIO.output(15, GPIO.LOW) # Set BIN1
    GPIO.output(16, GPIO.HIGH) # Set BIN2

    # Set the motor speed
    # Motor A:
    GPIO.output(29, GPIO.HIGH) # Set PWMA
    # Motor B:
    GPIO.output(18, GPIO.HIGH) # Set PWMB

    # Disable STBY (standby)
    GPIO.output(13, GPIO.HIGH)

    # Wait 5 seconds
    time.sleep(sec)
    GPIO.cleanup()

# Drive the motor counterclockwise
def reverse(sec):
    
    # Motor A:
    GPIO.output(12, GPIO.LOW) # Set AIN1
    GPIO.output(11, GPIO.HIGH) # Set AIN2
    # Motor B:
    GPIO.output(15, GPIO.HIGH) # Set BIN1
    GPIO.output(16, GPIO.LOW) # Set BIN2

    # Set the motor speed
    # Motor A:
    GPIO.output(29, GPIO.HIGH) # Set PWMA
    # Motor B:
    GPIO.output(18, GPIO.HIGH) # Set PWMB

    # Disable STBY (standby)
    GPIO.output(13, GPIO.HIGH)

    # Wait 5 seconds
    time.sleep(sec)
    GPIO.cleanup()


#Drive left
def left(sec): 
    
    # Motor A:
    GPIO.output(12, GPIO.HIGH) # Set AIN1
    GPIO.output(11, GPIO.LOW) # Set AIN2
    # Motor B:
    GPIO.output(15, GPIO.HIGH) # Set BIN1
    GPIO.output(16, GPIO.LOW) # Set BIN2

    # Set the motor speed
    # Motor A:
    GPIO.output(29, GPIO.HIGH) # Set PWMA
    # Motor B:
    GPIO.output(18, GPIO.HIGH) # Set PWMB

    # Disable STBY (standby)
    GPIO.output(13, GPIO.HIGH)

    # Wait 5 seconds
    time.sleep(sec)
    shutdown()
    GPIO.cleanup()

def right(sec):
    
    #Motor A:
    GPIO.output(12, GPIO.LOW) # Set AIN1
    GPIO.output(11, GPIO.HIGH) # Set AIN2
    # Motor B:
    GPIO.output(15, GPIO.LOW) # Set BIN1
    GPIO.output(16, GPIO.HIGH) # Set BIN2

    # Set the motor speed
    # Motor A:
    GPIO.output(29, GPIO.HIGH) # Set PWMA
    # Motor B:
    GPIO.output(18, GPIO.HIGH) # Set PWMB

    # Disable STBY (standby)
    GPIO.output(13, GPIO.HIGH)

    # Wait 5 seconds
    time.sleep(sec)
    shutdown()
    GPIO.cleanup()


def shutdown():
    GPIO.output(12, GPIO.LOW) # Set AIN1
    GPIO.output(11, GPIO.LOW) # Set AIN2
    GPIO.output(29, GPIO.LOW) # Set PWMA
    GPIO.output(13, GPIO.LOW) # Set STBY
    GPIO.output(15, GPIO.LOW) # Set BIN1
    GPIO.output(16, GPIO.LOW) # Set BIN2
    GPIO.output(18, GPIO.LOW) # Set PWMB





def hcsr():
    try:
        PIN_TRIGGER = 36
    	PIN_ECHO = 24
    	GPIO.setup(PIN_TRIGGER, GPIO.OUT)
    	GPIO.setup(PIN_ECHO, GPIO.IN)
    	GPIO.output(PIN_TRIGGER, GPIO.LOW)

    	print "sensor is calibrating..."
    	time.sleep(2)
    	print "Calculating distance"

    	GPIO.output(PIN_TRIGGER, GPIO.HIGH)

    	time.sleep(0.00001)

    	GPIO.output(PIN_TRIGGER, GPIO.LOW)

    	while GPIO.input(PIN_ECHO)==0:
            pulse_start_time = time.time()
    	while GPIO.input(PIN_ECHO)==1:
            pulse_end_time = time.time()

    	pulse_duration = pulse_end_time - pulse_start_time
    	distance = round(pulse_duration * 17150, 2)
    	print "Distance:",distance,"cm"
        


        while distance < 25:
            print('reverse,left', distance)
            init()
            reverse(.5)
            if distance < 25:
                print('left', distance)
                init()
                left(.5)
                init()
                reverse(.5)
                if distance < 25:
                    sys.exit()

            else:
                print("forward")
                init()
                forward(.55)
        
       # GPIO.cleanup()

    except:
        distance = 90
        print("Exception caught")
        GPIO.cleanup()
       
def main():
    init()
    hcsr()
    #GPIO.cleanup()


GPIO.cleanup()
if __name__ == '__main__':
    main()


