from serial.tools.list_ports import comports
from serial import Serial, SerialException, SerialTimeoutException
from serial.serialutil import PortNotOpenError
from colorama import Fore, init; init(autoreset=True)
# import serial

class Print:
    def error(*args, a=False):
        argument = " ".join(args)
        out = f"{Fore.LIGHTRED_EX}{argument}"
        print(out)
        if a:
            return out
    def info(*args):
        argument = " ".join(args)
        print(f"{Fore.CYAN}{argument}")
    def list_(*args):
        argument = " ".join(args)
        print(f"{Fore.LIGHTCYAN_EX}{argument}")
    def answer(*args):
        argument = " ".join(args)
        print(f"{Fore.LIGHTGREEN_EX}{argument}")

class Connection(Serial):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def getData(self):
        "read data from serial port"
        try:
            return self.readline().decode('utf-8').removesuffix("\r\n")
        except SerialException as e:
            Print.error(str(e))
    def writeData(self, data: str):
        "write data to serial port"
        try:
            self.write(data=data.encode('utf-8'))
        except SerialException as e:
            Print.error(str(e))
    def writeAndRead(self, data: str):
        "write data to serial port and return the response"
        self.writeData(data)
        return self.getData()
    @property
    def closeConnection(self):
        "close connection if opened"
        if self.isOpen():
            return True
        else:
            Print.info("Connection has already been terminated")
            return False
    @property
    def handOver(self):
        "hand over the raw object of serial connection --- Useless"
        return self
    
if __name__ == "__main__":
    Print.info("There are following ports available...")
    for port in comports():
        Print.list_(str(port))
    print()
    
    Print.info("Choose Following Configuration")
    port = "COM" + input("[PORT][COM4], COM").strip()
    if port == 'COM':
        port = 'COM4'
    baudrate = input("[BAUDRATE] [115200] ")
    if baudrate == '':
        baudrate = 115200
    elif baudrate.isdigit():
        baudrate = int(baudrate)
    else:
        raise SerialException(Print.error("Provided Baudrate is invalid. Expected <class 'int'> got {}".format(type(baudrate)), True))
    try:
        Print.info(f"\nAttemting connection on PORT {port} with baudrate of {baudrate}\n")
        serial_connection = Connection(port, baudrate)
    except SerialTimeoutException:
        Print.error("Connection timeout")
    except PortNotOpenError:
        Print.error(f"PORT {port} is currently busy")
    except SerialException as e:
        Print.error(e.__class__.__name__, str(e))
        exit()
    while True:
        res = serial_connection.writeAndRead(input("What is your message? "))
        if res != '':
            Print.answer(res)
