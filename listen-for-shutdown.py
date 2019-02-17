## crear el presente archivo: sudo nano listen-for-shutdown.py

#!/usr/bin/env python


import RPi.GPIO as GPIO
import subprocess


GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.wait_for_edge(3, GPIO.FALLING)

subprocess.call(['shutdown', '-h', 'now'], shell=False)

##ponerlo en: /usr/local/bin y habilitar ejecucion.

#sudo mv listen-for-shutdown.py /usr/local/bin/
#sudo chmod +x /usr/local/bin/listen-for-shutdown.py

