from pyfirmata import Arduino, util
import time


def irrigation():
    """
    Function that performs communication with the arduino and infinitely checks the status of the ground
    :return:
    """
    try:
        Board = Arduino('COM4')  # Defines the port where the Arduino is
        it = util.Iterator(Board)  # Controls arduino port readings
        it.start()  # Starts communication with the arduino.

        # Sets relay pins to OUTPUT
        Board.get_pin('d:10:o')

        # relay starts off
        Board.digital[10].write(1)

        # Defines analog port -> sensor
        valor_analog = Board.get_pin('a:0:i')

        time.sleep(0.5)

        while True:
            # Value the sensor read
            valor_analogico = valor_analog.read()

            if 0 < valor_analogico < 0.5:  # If soil is wet
                print("STATUS: Moist soil - {} \n".format(valor_analogico))

            elif 0.5 < valor_analogico < 0.8:  # If the solo is normal
                print("STATUS: Solo moderado - {} \n".format(valor_analogico))

            elif 0.8 < valor_analogico <= 1:  # If the soil is dry
                print(" \nSTATUS: Dry soil - {}\n".format(valor_analogico))
                Board.digital[10].write(0)  # turn on the relay
                print("WATERING...")
                time.sleep(2.5)  # Hold open for 3 seconds
                Board.digital[10].write(1)  # turn off the relay
                print("SUCCESSFULLY WATERED PLANTS!!!")

            time.sleep(60)  # 3 sec delay, then the loop repeats

    except Exception as e:
        print(e)
