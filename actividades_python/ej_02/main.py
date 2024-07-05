import RPi.GPIO as GPIO
import time

PULSADOR_PIN = 18   # Pin GPIO utilizado para el pulsador
LED_ROJO_PIN = 19    # Pin GPIO utilizado para el LED rojo
LED_VERDE_PIN =13   # Pin GPIO utilizado para el LED verde
LED_AZUL_PIN = 16    # Pin GPIO utilizado para el LED azul

# Configuración de los pines GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(PULSADOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Pulsador con resistencia pull-up interna
GPIO.setup(LED_ROJO_PIN, GPIO.OUT)
GPIO.setup(LED_VERDE_PIN, GPIO.OUT)
GPIO.setup(LED_AZUL_PIN, GPIO.OUT)

# Función para controlar el estado de los LEDs
def control_led_rgb(led_pin, estado):
    GPIO.output(led_pin, estado)

try:
    while True:
        # Espera a que se presione el pulsador
        GPIO.wait_for_edge(PULSADOR_PIN, GPIO.FALLING)
        
        # Enciende el LED rojo
        control_led_rgb(LED_ROJO_PIN, GPIO.HIGH)
        time.sleep(1)  # Mantiene el LED rojo encendido durante 1 segundo
        
        # Apaga el LED rojo
        control_led_rgb(LED_ROJO_PIN, GPIO.LOW)
        
        # Enciende el LED verde
        control_led_rgb(LED_VERDE_PIN, GPIO.HIGH)
        time.sleep(0.5)  # Mantiene el LED verde encendido durante 0.5 segundos
        
        # Apaga el LED verde
        control_led_rgb(LED_VERDE_PIN, GPIO.LOW)
        
        # Enciende el LED azul
        control_led_rgb(LED_AZUL_PIN, GPIO.HIGH)
        time.sleep(0.25)  # Mantiene el LED azul encendido durante 0.25 segundos
        
        # Apaga el LED azul
        control_led_rgb(LED_AZUL_PIN, GPIO.LOW)

finally:
    GPIO.cleanup()
