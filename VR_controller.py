"""VR Controller is an object which interfaces with the "VR v2" """

import time

serial_imported = True

try:
    import serial
except ImportError:
    serial_imported = False


class VR_controller:
    def __init__(self):

        if(serial_imported == False):
            print("Serial is not Installed")
        else:
            self.ser = serial.Serial(
                        port='/dev/ttyAMA0',
                        baudrate = 9600,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE,
                        bytesize=serial.EIGHTBITS,
                        timeout=5)
            print("Serial Port instantiated!")
        self.commands = {"wait": b"\x00",
                    "del_1": b"\x01",
                    "del_2 ": b"\x02",
                    "del_3": b"\x03",
                    "del_all": b"\x04",
                    "begin_rec_1": b"\x11",
                    "begin_rec_2": b"\x12",
                    "begin_rec_3": b"\x13",
                    "import_1": b"\x21",
                    "import_2": b"\x22",
                    "import_3": b"\x23",
                    "query_all": b"\x24",
                    "baud_2400": b"\x31",
                    "baud_4800": b"\x32",
                    "baud_9600": b"\x33",
                    "baud_19200": b"\x34",
                    "baud_38400": b"\x35",
                    "mode_common": b"\x36",
                    "mode_compact": b"\x37",
                    "reset_1": b"\x41",
                    "reset_2": b"\x42",
                    "reset_3": b"\x43",
                    "reset_4": b"\x44",
                    "reset_5": b"\x45",
                    "reset_all": b"\x46",
                    "mode_pulse": b"\x50",
                    "mode_flip": b"\x51",
                    "mode_down": b"\x52",
                    "mode_up": b"\x53",
                    "pulse_time_10ms": b"\x60",
                    "pulse_time_15ms": b"\x61",
                    "pulse_time_20ms": b"\x62",
                    "pulse_time_25ms": b"\x63",
                    "pulse_time_30ms": b"\x64",
                    "pulse_time_50ms": b"\x65",
                    "pulse_time_60ms": b"\x66",
                    "pulse_time_70ms": b"\x67",
                    "pulse_time_80ms": b"\x68",
                    "pulse_time_90ms": b"\x69",
                    "pulse_time_100ms": b"\x6a",
                    "pulse_time_200ms": b"\x6b",
                    "pulse_time_300ms": b"\x6c",
                    "pulse_time_400ms": b"\x6d",
                    "pulse_time_500ms": b"\x6e",
                    "pulse_time_1000ms": b"\x6f",
                    "reset": b"\x70",
                    "version": b"\xbb"
                    }

    def send_command(self, command):
        if isinstance(command, bytes):
            if serial_imported == False:
                print("Serial Library Not Installed")
                return -1

            else:
                command = b"\xaa" + command
                self.ser.write(command)
                print(command)
                time.sleep(0.5)
                while (1):
                    time.sleep(2.5)
                    x = self.ser.readline()
                    print(x)
                    if x==b'':
                        break
                return
        else:
            print('Paramemter needs to be of type "byte"')

    def record_group(self, group_num):
        command = self.commands["begin_rec_" + str(group_num)]
        self.send_command(command)

