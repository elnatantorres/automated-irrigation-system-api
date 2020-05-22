from pyfirmata import Arduino, util
import time

board = Arduino('COM13')  # Define a porta onde esta o arduino
it = util.Iterator(board)  # Controla as leituras das portas do arduino
it.start()

# Define porta analogica -> sensor
pino_analogico = board.get_pin('a:0:i')

# Defino pinos do 10 ao 13 como OUTPUT
pino10 = board.get_pin('d:10:o')
pino11 = board.get_pin('d:11:o')
pino12 = board.get_pin('d:12:o')
pino13 = board.get_pin('d:13:o')

# Desliga pinos 10 ao 13, write(0) => LOW
desliga_pino11 = board.digital[10].write(0)
desliga_pino12 = board.digital[11].write(0)
desliga_pino13 = board.digital[12].write(0)
desliga_pino14 = board.digital[13].write(0)

# Define pinos do rele como OUTPUT
pino_rele = board.get_pin('d:4:o')
pino_rele2 = board.get_pin('d:3:o')

# Reles iniciam desligados
board.digital[4].write(1)
board.digital[3].write(1)

time.sleep(2)
while True:
    valor_analogico = pino_analogico.read()  # Valor que o sensor leu

    if 0 <= valor_analogico <= 340:  # Caso solo esteja umido
        print("STATUS: Solo umido")

    elif 681 >= valor_analogico >= 341:  # Caso solo esteja normal
        print("STATUS: Solo moderado")

    elif 1023 >= valor_analogico >= 682:  # Caso o solo esteja seco
        print("STATUS: Solo seco")
        board.digital[3].write(0)
        time.sleep(2)  # Mantem aberta por 2 segundos
        board.digital[3].write(1)  # desliga o rele

    time.sleep(3)  # Delay de 3 seg, depois o loop se repete
