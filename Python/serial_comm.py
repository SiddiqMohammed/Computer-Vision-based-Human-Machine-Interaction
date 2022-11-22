# Edit the arduino file named "relay_test"
import serial
import time

arduinoData = serial.Serial('com3', 115200)
time.sleep(3)

pauseTime = 1  # in seconds


def send_value_to_arduino(x):
    # value_to_send = bytes([x])

    arduinoData.write(x.encode('utf-8'))
    arduinoData.close()
    print("X")

    time.sleep(pauseTime)
    # print(value_to_send)

# send_value_to_arduino("1")