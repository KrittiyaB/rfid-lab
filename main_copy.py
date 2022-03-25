#!/usr/bin/python3
import codecs
import sys
import time

import serial


class ReadLine:
    def __init__(self, s):
        self.buf = bytearray()
        self.s = s

    # def readline(self):
    #     # i = self.buf.find(b"\n")
    #     # if i >= 0:
    #     #     r = self.buf[:i + 1]
    #     #     self.buf = self.buf[i + 1:]
    #     #     return r
    #     while True:
    #         i = max(1, min(2048, self.s.in_waiting))
    #         data = self.s.read(i)
    #         i = data.find(b"\n")
    #         if i >= 0:
    #             r = self.buf + data[:i + 1]
    #             self.buf[0:] = data[i + 1:]
    #             return r
    #         else:
    #             self.buf.extend(data)


if __name__ == '__main__':
    try:
        serial_instance = serial.serial_for_url(
            '/dev/cu.usbserial-0001',
            9600,
            parity='N',
            do_not_open=True)
        serial_instance.open()
        if serial_instance.is_open:
            print('open')
            count = 1
            serial_instance.write(b'\x43\x03\x01')
            lines = ''
            time.sleep(5)
            b = serial_instance.read(serial_instance.inWaiting())
            print(b.hex())

            # while serial_instance.isOpen():
            #     for l in serial_instance.readline(1):
            #         lines = lines + ' ' + hex(l)
            #         # print(str(count) + str(': ') + chr(line))
            #         # count = count + 1
            #     print(lines)

        # r = ReadLine(serial_instance)
        # serial_instance.write(b'0x43 0x03 0x01')
        # r.readline()
    except serial.SerialException as e:
        sys.stderr.write('could not open port {!r}: {}\n'.format('/dev/cu.usbserial-0001', e))
