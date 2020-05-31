import time
from pyfirmata import Arduino, util

Board = Arduino('COM4')  # Define a porta onde esta o arduino
it = util.Iterator(Board)  # Controls arduino port readings
it.start()  # Starts communication with the arduino.

# Define pino do rele como OUTPUT
pino_rele = Board.get_pin('d:10:o')

Board.digital[10].write(1)  # Rele inicia desligado

# Define porta analogica -> sensor
valor_analog = Board.get_pin('a:0:i')

time.sleep(0.5)

while True:
    valor_analogico = valor_analog.read()  # Valor que o sensor leu

    if 0 < valor_analogico < 0.5:  # Caso solo esteja umido
        print("\nSTATUS: Solo umido - {} \n".format(valor_analogico))

    elif 0.5 < valor_analogico < 0.8:  # Caso solo esteja normal
        print("\nSTATUS: Moderate soil - {} \n".format(valor_analogico))

    elif 0.8 < valor_analogico <= 1:  # Caso o solo esteja seco
        print("\nSTATUS: Solo seco - {}\n".format(valor_analogico))
        Board.digital[10].write(0)
        print("REGANDO...")
        time.sleep(2.5)  # Mantem aberta por 2 segundos
        Board.digital[10].write(1)  # desliga o rele
        print("PLANTAS REGADAS COM SUCESSO!!!")

    time.sleep(10)  # Delay de 3 seg, depois o loop se repete
