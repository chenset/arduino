from time import sleep
import serial

# ser = serial.Serial('COM3', baudrate=9600, timeout=1)  # Establish the connection on a specific port
ser = serial.Serial('/dev/ttyUSB0', baudrate=9600, timeout=1)  # Establish the connection on a specific port
counter = 32  # Below 32 everything in ASCII is gibberish
while True:
    counter += 1
    # ser.write(bytes(((counter))))  # Convert the decimal number to ASCII then send it to the Arduino
    print(str(ser.readline()))  # Read the newest output from the Arduino
    sleep(1)  # Delay for one tenth of a second
    if counter == 255:
        counter = 32
