from serial import Serial
from serial import SerialException
from serial.tools.list_ports import comports

def check_bl(port):
    try:
        ser = Serial(port.device,baudrate=1200,timeout=2)
        ser.close()
        return True
    except SerialException:
        return False

def scan():
    ports = comports()

    if len(ports) == 0:
            print("No available COM ports found.")
    else:
        for port in ports:
            if check_bl(port):
                print(port,"\t[Bootloader]")
            else:
                print(port)