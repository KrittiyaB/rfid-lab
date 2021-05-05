import csv
import os
from datetime import datetime

import pandas as pd


def write_result(data, timestamp):
    # create log file from date
    file = '../data/experiment_temp_{}.csv'.format(datetime.now().strftime("%Y%m%d"))
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


def get_temp(t):
    t_range = 0
    if int(t) in range(20, 23):
        t_range = 21
    elif int(t) in range(24, 27):
        t_range = 25
    elif int(t) in range(28, 31):
        t_range = 29
    elif int(t) in range(32, 35):
        t_range = 33
    elif int(t) in range(36, 39):
        t_range = 37

    return t_range


def extract_data():
    df = pd.read_excel('../data/RFID_DATASET_NOTEMP.xlsx')
    new_df = pd.DataFrame(
        columns=['TagNo', 'Distance', 'Temperature', 'RealTemp', 'RSSI', 'FREQ', 'H_RSSI', 'H_FREQ', 'ID', 'Data',
                 'Detect'])
    print(df)
    df['Data'] = df['Data'].astype('str')

    for index, row in df.iterrows():
        new_df.at[index, 'TagNo'] = row['TagNo']
        new_df.at[index, 'Distance'] = row['Distance']
        new_df.at[index, 'RealTemp'] = row['ExpTemp']
        new_df.at[index, 'Temperature'] = get_temp(row['ExpTemp'])

        if row['Data'] != '4405000000':
            data = row['Data']
            # print(data[6:8] + " " + data[8:14] + " " + data[20:])
            new_df.at[index, 'Data'] = data
            new_df.at[index, 'H_RSSI'] = data[6:8]  # QI
            new_df.at[index, 'H_FREQ'] = data[8:14]
            new_df.at[index, 'ID'] = data[20:]
            new_df.at[index, 'Detect'] = 1
        else:
            new_df.at[index, 'Data'] = row['Data']
            new_df.at[index, 'H_RSSI'] = None
            new_df.at[index, 'H_FREQ'] = None
            new_df.at[index, 'ID'] = None
            new_df.at[index, 'Detect'] = 0

    print(new_df.head(10))
    rssi_to_dec(new_df)
    # new_df.to_csv('../src/extracted_data.csv', index=False)


def rssi_to_dec(df):
    df['H_FREQ'] = df['H_FREQ'].fillna(0)
    df['H_FREQ'] = df['H_FREQ'].astype('str')
    df['H_RSSI'] = df['H_RSSI'].fillna(0)
    df['H_RSSI'] = df['H_RSSI'].astype('str')

    for index, row in df.iterrows():
        df.at[index, 'FREQ'] = int(row['H_FREQ'], 16)
        df.at[index, 'RSSI'] = int(row['H_RSSI'], 16)

    print(df.head(10))
    df.to_csv('../data/RFID_DATA_SET_NOTEMP_CLEANED.csv', index=False)


if __name__ == '__main__':
    # barr = b'\x44\x05\x00\x00\x00'
    # write_result(barr, datetime.now())
    extract_data()
    # rssi_to_dec()
