# Edit the arduino file named "relay_test"
import serial
import time

arduinoData = serial.Serial('com3', 9600)
pauseTime = 1  # in seconds


def send_value_to_arduino(x):
    value_to_send = x
    while 1:
        value_to_send = not value_to_send

        if value_to_send == 0:
            time.sleep(pauseTime)
            arduinoData.write(b'0')
            print("X")

        if value_to_send == 1:
            time.sleep(pauseTime)
            arduinoData.write(b'1')
            print("E")

        time.sleep(pauseTime)
        print(value_to_send)

