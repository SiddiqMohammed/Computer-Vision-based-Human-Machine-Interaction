# Edit the arduino file named "relay_test"
# Make sure this is pyserial not default one
import serial
import time

arduinoData = serial.Serial('com3', 115200)

# set these to false for esp32
arduinoData.setDTR(False)
arduinoData.setRTS(False)

pauseTime = 1  # in seconds

time.sleep(3) # Need time to establish connection
def send_value_to_arduino(x):
    x = str(x)
    arduinoData.write(x.encode('utf-8'))


    # time.sleep(pauseTime)

# send_value_to_arduino(20)