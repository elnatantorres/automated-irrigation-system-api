from pyfirmata import Arduino, util
import time


def excution_irrigation():
    """
    Performs irrigation regardless of soil condition.
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
        Board.get_pin('a:0:i')

        time.sleep(0.5)

        Board.digital[10].write(0)  # turn on the relay
        time.sleep(2.5)  # Hold open for 3 seconds
        Board.digital[10].write(1)  # turn off the relay

    except Exception as e:
        print(e)
