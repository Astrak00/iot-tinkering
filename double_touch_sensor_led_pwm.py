from RPi import GPIO
from time import sleep

print("remember to use python3.11 not python3.13 or de default python3!!!!")


LED_PIN             = 12
TOUCH_INCREMENT_PIN = 2
TOUCH_DECREMENT_PIN = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(TOUCH_INCREMENT_PIN, GPIO.IN)
GPIO.setup(TOUCH_DECREMENT_PIN, GPIO.IN)

GPIO.setup(LED_PIN, GPIO.OUT)
pwm = GPIO.PWM(LED_PIN, 100)  # Set up PWM on LED_PIN with 100Hz frequency
pwm.start(0)  # Start PWM with 0% duty cycle

pwn_state = 0

try:
        # If increment button is pressed, increment the counter by 20
        while True:
            if GPIO.input(TOUCH_INCREMENT_PIN) == GPIO.HIGH:
                pwn_state += 20
                if pwn_state > 100: # PWM must be between 0.0 and 100.0
                    pwn_state = 100
                pwm.ChangeDutyCycle(pwn_state)
                print("Incremented to", pwn_state)
            if GPIO.input(TOUCH_DECREMENT_PIN) == GPIO.HIGH:
                pwn_state -= 20
                if pwn_state < 0:
                    pwn_state = 0
                pwm.ChangeDutyCycle(pwn_state)
                print("Decremented to", pwn_state)
            sleep(0.15)
finally:
        GPIO.cleanup()

