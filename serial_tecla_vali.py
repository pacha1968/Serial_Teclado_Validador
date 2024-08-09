from machine import Pin, UART
import time

#Teclado
# Configura UART0 con pines 1 (TX) y 2 (RX) - predeterminados
t_uart0 = UART(0, baudrate=9600, tx=Pin(1), rx=Pin(2))


#Validador
# Configura UART1 con pines 6 (TX) y 7 (RX)
v_uart1 = UART(1, baudrate=9600, tx=Pin(6), rx=Pin(7))


while True:
    # Lee datos de UART0(Teclado)
    if t_uart0.any():
        data_teclado = t_uart0.read()  #Muestra datos del Teclado
        print("UART0:", data_teclado)

    # Lee datos de UART1(Validador)
    if v_uart1.any():
        data_validador = v_uart1.read()
        print("UART1:", data_validador) #Muestra datos del Validador

    time.sleep(0.1)  