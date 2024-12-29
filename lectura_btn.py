#!/usr/bin/env python3
from gpiozero import Button
import time

# Inicializa el botón conectado al pin GPIO 22
BtnPin = Button(22)

try:
    # Bucle principal para leer e imprimir valores del ADC y el estado del botón
    while True:
        # Leer el estado del botón (presionado o no)
        Btn_val = BtnPin.value

        # Imprimir los valores de X, Y y el botón
        # print('Btn: %d' % ( Btn_val))
        print(f'Btn: {Btn_val}')

        # Esperar 0.2 segundos antes de la siguiente lectura
        time.sleep(0.2)

# Manejar la terminación del script de manera elegante (por ejemplo, con KeyboardInterrupt)
except KeyboardInterrupt:
    pass

