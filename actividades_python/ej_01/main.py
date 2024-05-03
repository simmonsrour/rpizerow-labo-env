import RPi.GPIO as GPIO   # 1. Importa la biblioteca RPi.GPIO para controlar los pines GPIO
import time              # 1. Importa la biblioteca time para manejar el tiempo

PULSADOR_PIN = 18   # 5. Define el pin GPIO utilizado para el pulsador
LED_PIN = 26        # 5. Define el pin GPIO utilizado para el LED

GPIO.setmode(GPIO.BCM)  # 7. Establece el modo GPIO en BCM
GPIO.setup(PULSADOR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # 8. Configura el pin del pulsador como entrada con resistencia pull-up
GPIO.setup(LED_PIN, GPIO.OUT)  # 8. Configura el pin del LED como salida

def control_led(estado):  # 11. Define una función para controlar el estado del LED
    GPIO.output(LED_PIN, estado)

try:
    while True:  # 14. Inicia un bucle infinito

        GPIO.wait_for_edge(PULSADOR_PIN, GPIO.FALLING)  # 17. Espera hasta que se detecte un flanco de bajada en el pin del pulsador

        control_led(True)  # 19. Enciende el LED cuando se presiona el pulsador
        GPIO.wait_for_edge(PULSADOR_PIN, GPIO.RISING)  # 20. Espera hasta que se detecte un flanco de subida en el pin del pulsador

        control_led(False)  # 22. Apaga el LED cuando se suelta el pulsador

except KeyboardInterrupt:
    GPIO.cleanup()  # 24. Limpia los pines GPIO al salir del programa
