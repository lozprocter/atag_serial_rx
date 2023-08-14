import serial, sys
from os import listdir

BAUD_RATE = 9600

def establish_connection(port):
    
    try:

        filesForDevice = listdir('/dev/') # put all device files into list[]

        for line in filesForDevice: # run through all files

            if sys.platform == 'darwin':

                if (line[:12] == 'tty.usbmodem'): # look for...   
                    print("hey")
                    devicePort = line # take whole line (includes suffix address e.g. ttyACM0
                    e = serial.Serial('/dev/' + str(devicePort), BAUD_RATE, timeout = 6, writeTimeout = 20) # assign

            # FLAG: This if statement is only relevant in linux environment. 
            # EITHER: USB Comms hardware
            # if (line[:6] == 'ttyUSB' or line[:6] == 'ttyACM'): # look for prefix of known success (covers both Mega and Uno)
            # OR: UART Comms hardware
            elif line[:7] == port: # looks specifically for USB port that encoder is plugged into
                devicePort = line # take whole line (includes suffix address e.g. ttyACM0
                e = serial.Serial('/dev/' + str(devicePort), BAUD_RATE, timeout = 6, writeTimeout = 20) # assign
                
        return e

    except: 
        print('No arduino connected')

def receiver(serial_obj): 
    if serial_obj.inWaiting():
        rec_temp = serial_obj.readline().decode('utf-8').upper().strip()
        return rec_temp
        
        
serial_obj_1 = establish_connection("")
print(serial_obj_1)

serial_obj_2 = establish_connection("")
print(serial_obj_2)

serial_obj_3 = establish_connection("")
print(serial_obj_3)

serial_obj_1.flushInput()
serial_obj_2.flushInput()
serial_obj_3.flushInput()

while True:
    with open("ATAG_CABLE_RESULTS.txt", "a") as f:
        line = receiver(serial_obj_1)
        if line:
            f.write(str(line))
            print(line)
        
    with open("ATAG_CABLE_RESULTS.txt", "a") as f:
        line = receiver(serial_obj_2)
        if line:
            f.write(str(line))
            print(line)
    with open("ATAG_CABLE_RESULTS.txt", "a") as f:
        line = receiver(serial_obj_3)
        if line:
            f.write(str(line))
            print(line)