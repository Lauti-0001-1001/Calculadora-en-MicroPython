import machine
from machine import Pin, Timer
import time
from lcd_i2c import LCD
from machine import I2C, Pin

NADA = 0
EVENTO = 1
ESPERA = 2

variable = None
variable2 = None
funcion = None
resultado = None
botonesListos = False

Uno = Pin(13, Pin.IN, Pin.PULL_UP)
Dos = Pin(12, Pin.IN, Pin.PULL_UP)
Tres = Pin(14, Pin.IN, Pin.PULL_UP)
Cuatro = Pin(27, Pin.IN, Pin.PULL_UP)
Cinco = Pin(26, Pin.IN, Pin.PULL_UP)
Seis = Pin(25, Pin.IN, Pin.PULL_UP)
Siete = Pin(33, Pin.IN, Pin.PULL_UP)
Ocho = Pin(32, Pin.IN, Pin.PULL_UP)
Nueve = Pin(22, Pin.IN, Pin.PULL_UP) 
Cero = Pin(23, Pin.IN, Pin.PULL_UP) 

suma = Pin(15, Pin.IN, Pin.PULL_UP)
resta = Pin(2, Pin.IN, Pin.PULL_UP)
Multiplicar = Pin(4, Pin.IN, Pin.PULL_UP)
dividir = Pin(5, Pin.IN, Pin.PULL_UP)

led1 = Pin(21, Pin.OUT)


estadoUno = NADA
estadoDos = NADA
estadoTres = NADA
estadoCuatro = NADA
estadoCinco = NADA
estadoSeis = NADA
estadoSiete = NADA
estadoOcho = NADA
estadoNueve = NADA
estadoCero = NADA
estadoSuma = NADA
estadoResta = NADA
estadoMultiplicar = NADA
estadoDividir = NADA

I2C_ADDR = 0x27
i2c = I2C(0, scl=Pin(18), sda=Pin(19), freq=800000)
lcd = LCD(addr=I2C_ADDR, cols=20, rows=4, i2c=i2c)
lcd.begin()
lcd.clear()





def procesaEntrada(estadoActual, valorPin):
    if estadoActual == NADA and valorPin == False:
        return EVENTO
    else:
        if estadoActual == EVENTO:
            return ESPERA
        else:
            if estadoActual == ESPERA and valorPin == False:
                return ESPERA
            else:
                return NADA

lcd.print("Ingrese 1er numero")
time.sleep(1)

while variable is None:
    estadoUno = procesaEntrada(estadoUno, Uno.value())
    estadoDos = procesaEntrada(estadoDos, Dos.value())
    estadoTres = procesaEntrada(estadoTres, Tres.value())
    estadoCuatro = procesaEntrada(estadoCuatro, Cuatro.value())
    estadoCinco = procesaEntrada(estadoCinco, Cinco.value())
    estadoSeis = procesaEntrada(estadoSeis, Seis.value())
    estadoSiete = procesaEntrada(estadoSiete, Siete.value())
    estadoOcho = procesaEntrada(estadoOcho, Ocho.value())
    estadoNueve = procesaEntrada(estadoNueve, Nueve.value())
    estadoCero = procesaEntrada(estadoCero, Cero.value())

    if estadoUno == EVENTO:
        variable = 1
    else:
        if estadoDos == EVENTO:
            variable = 2
        else:
            if estadoTres == EVENTO:
                variable = 3
            else:
                if estadoCuatro == EVENTO:
                    variable = 4
                else:
                    if estadoCinco == EVENTO:
                        variable = 5
                    else:
                        if estadoSeis == EVENTO:
                            variable = 6
                        else:
                            if estadoSiete == EVENTO:
                                variable = 7
                            else:
                                if estadoOcho == EVENTO:
                                    variable = 8
                                else:
                                    if estadoNueve == EVENTO:
                                        variable = 9
                                    else:
                                        if estadoCero == EVENTO:
                                            variable = 0
    time.sleep_ms(50)

lcd.clear()
lcd.print("Elija operacion:")
time.sleep(1)

while funcion is None:
    estadoSuma = procesaEntrada(estadoSuma, suma.value())
    estadoResta = procesaEntrada(estadoResta, resta.value())
    estadoMultiplicar = procesaEntrada(estadoMultiplicar, Multiplicar.value())
    estadoDividir = procesaEntrada(estadoDividir, dividir.value())

    if estadoSuma == EVENTO:
        funcion = 1
    else:
        if estadoResta == EVENTO:
            funcion = 2
        else:
            if estadoMultiplicar == EVENTO:
                funcion = 3
            else:
                if estadoDividir == EVENTO:
                    funcion = 4
    time.sleep_ms(50)

lcd.clear()
lcd.print("Ingrese 2do numero")
time.sleep(1)

while variable2 is None:
    estadoUno = procesaEntrada(estadoUno, Uno.value())
    estadoDos = procesaEntrada(estadoDos, Dos.value())
    estadoTres = procesaEntrada(estadoTres, Tres.value())
    estadoCuatro = procesaEntrada(estadoCuatro, Cuatro.value())
    estadoCinco = procesaEntrada(estadoCinco, Cinco.value())
    estadoSeis = procesaEntrada(estadoSeis, Seis.value())
    estadoSiete = procesaEntrada(estadoSiete, Siete.value())
    estadoOcho = procesaEntrada(estadoOcho, Ocho.value())
    estadoNueve = procesaEntrada(estadoNueve, Nueve.value())
    estadoCero = procesaEntrada(estadoCero, Cero.value())

    if estadoUno == EVENTO:
        variable2 = 1
    else:
        if estadoDos == EVENTO:
            variable2 = 2
        else:
            if estadoTres == EVENTO:
                variable2 = 3
            else:
                if estadoCuatro == EVENTO:
                    variable2 = 4
                else:
                    if estadoCinco == EVENTO:
                        variable2 = 5
                    else:
                        if estadoSeis == EVENTO:
                            variable2 = 6
                        else:
                            if estadoSiete == EVENTO:
                                variable2 = 7
                            else:
                                if estadoOcho == EVENTO:
                                    variable2 = 8
                                else:
                                    if estadoNueve == EVENTO:
                                        variable2 = 9
                                    else:
                                        if estadoCero == EVENTO:
                                            variable2 = 0
    time.sleep_ms(50)

if funcion == 1:
    resultado = variable + variable2
    operacion_texto = "Suma"
else:
    if funcion == 2:
        resultado = variable - variable2
        operacion_texto = "Resta"
    else:
        if funcion == 3:
            resultado = variable * variable2
            operacion_texto = "Multiplicacion"
        else:
            if funcion == 4:
                if variable2 == 0:
                    resultado = "Error div/0"
                else:
                    resultado = variable / variable2
                operacion_texto = "Division"
            else:
                resultado = "Error"
                operacion_texto = "Desconocida"



lcd.clear()
lcd.print("Op: " + operacion_texto)
lcd.set_cursor(0, 1)
lcd.print("Res: " + str(resultado))
led1.value(1)
