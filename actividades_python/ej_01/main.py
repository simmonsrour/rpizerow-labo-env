import RPi.GPIO as GPIO
import time

PULSADOR_PIN = 18
LED_PIN = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(PULSADOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_PIN, GPIO.OUT)

def control_led(estado):
    GPIO.output(LED_PIN, estado)

try:
    while True:

        GPIO.wait_for_edge(PULSADOR_PIN, GPIO.FALLING)

        control_led(True)
        GPIO.wait_for_edge(PULSADOR_PIN, GPIO.RISING)

        control_led(False)

except KeyboardInterrupt:
    GPIO.cleanup()
