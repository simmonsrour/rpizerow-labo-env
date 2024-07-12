from gpiozero import LED, Buzzer
from time import sleep

rojo = LED(19)
verde = LED(13)
azul = LED(26)
buzz = Buzzer (22)

while True:
	comando = input ("Ingrese comando [buzz ; rgb , quit]:")
	func = input ("Ingrese funcion [on ; off ; green ; red ; blue]:")
	if  comando == 'buzz':
		if func == 'on':
			buzz.on()
		if func == 'off':
			buzz.off()
	if comando == 'rgb':
		if func == 'green':
			verde.toggle()
		if func == 'red':
			rojo.toggle()
		if func == 'blue':
			azul.toggle()
	if comando == 'quit':
		break
