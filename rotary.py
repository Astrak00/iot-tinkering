from RPi import GPIO
from time import sleep

CLK_PIN_ROTARY  = 27
DT_PIN_ROTARY   = 22 

GPIO.setmode(GPIO.BCM)
GPIO.setup(CLK_PIN_ROTARY, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(DT_PIN_ROTARY, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

counter = 0
clkLastState = GPIO.input(CLK_PIN_ROTARY)

try:
        while True:
                clkState = GPIO.input(CLK_PIN_ROTARY)
                dtState = GPIO.input(DT_PIN_ROTARY)
                if clkState != clkLastState:
                        clkLastState = clkState
                        if dtState != clkState:
                                counter += 1
                        else:
                                counter -= 1
                        print(counter)
                sleep(0.001)
finally:
        GPIO.cleanup()
