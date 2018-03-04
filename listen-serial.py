import serial

serialport = serial.Serial("/dev/ttyAMA0", 9600, timeout=0.5)

while True:    
        command = serialport.read()
        print str(command)
