import os
import time
import ADS1x15
import math
from gpiozero import PWMLED

# choose your sensor
# ADS = ADS1x15.ADS1013(1, 0x48)
# ADS = ADS1x15.ADS1014(1, 0x48)
# ADS = ADS1x15.ADS1015(1, 0x48)
# ADS = ADS1x15.ADS1113(1, 0x48)
# ADS = ADS1x15.ADS1114(1, 0x48)

ADS = ADS1x15.ADS1115(1, 0x48)

print(os.path.basename(_file_))
print("ADS1X15_LIB_VERSION: {}".format(ADS1x15._version_))

# set gain to 4.096V max
ADS.setGain(ADS.PGA_4_096V)
f = ADS.toVoltage()

k = 0.2

azul = PWMLED(26)
rojo = PWMLED(19)

while True :
    val_ter = ADS.readADC(1)
    val_pot = ADS.readADC(3)
    volt_term = val_ter * f

    temp_pot = 30 * val_pot / 32767.5
    res_ter = (volt_term * 10000) / (3.3 - volt_term)
    temp_term = (298 * 3900) / (298 * math.log(res_ter / 10000) + 3900) - 273.15

    print(temp_term)
    print(temp_pot)

    dif = temp_term - temp_pot

    if dif > 0:
        if dif >= 5:
            dif = 5
        azul.value = dif * k
        rojo.off()
    elif dif < 0:
        if dif <= -5:
            dif = -5
        rojo.value = dif * k * -1
        azul.off()


    time.sleep(1)
