import csv
import os
from datetime import datetime


def write_result(data, timestamp):
    # create log file from date
    file = 'experiment_{}.csv'.format(datetime.now().strftime("%Y%m%d"))
    hex_data = data.hex()
    d = [hex_data, timestamp]
    if not os.path.exists(file):
        fields = ['Data', 'Timestamp']
        with open(file, 'a') as f:
            writer = csv.writer(f)
            writer.writerow(fields)
            writer.writerow(d)
    else:
        with open(file, 'a') as f:
            writer = csv.writer(f)
            writer.writerow(d)


if __name__ == '__main__':
    barr = b'\x44\x05\x00\x00\x00'
    write_result(barr, datetime.now())
