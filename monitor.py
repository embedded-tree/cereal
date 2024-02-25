import sys
import ports
import commands.help as help
import commands.version as version
import serial
from time import sleep

com = 'COM3'
baud = 9600
monitor = False

def sl_attempt():
    try:
        ser = serial.Serial(com, baud, timeout=.2)
        print("Serial connection opened in port: ",com," and baud rate: ",baud)
        while monitor:
            if ser.in_waiting > 0:
                try:
                    serd = ser.readline().decode('utf-8','ignore').strip()
                    print("> ",serd)
                except Exception as readExc:
                    print("Error: ",readExc)
    except KeyboardInterrupt:
        sys.exit()

if len(sys.argv) < 2:
    help.default()
    sys.exit(1)

if sys.argv[1] == "ports":
    print(ports.scan())
elif sys.argv[1] == "serial":
    if len(sys.argv) < 4:
        monitor = True
        sl_attempt()
    else:
        com = str(sys.argv[2])
        baud = int(sys.argv[3])
        monitor = True
        sl_attempt()
        
elif sys.argv[1] == "version" or sys.argv[1] == "--version":
    if len(sys.argv) < 3:
        print(version.fetch().version)