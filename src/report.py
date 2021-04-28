import csv
import os
from datetime import datetime

import pandas as pd


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


def extract_data():
    df = pd.read_csv('../data/data.csv')
    # print(df.head(5)
    new_df = pd.DataFrame(columns=['Data', 'QI', 'Frequency', 'ID'])
    print(df)

    for index, row in df.iterrows():
        # print(row['Data'])
        if row['Data'] != '4405000000':
            data = row['Data']
            # print(data)
            # print(data[6:8] + " " + data[8:14] + " " + data[20:])
            new_df.at[index, 'Data'] = data
            new_df.at[index, 'QI'] = data[6:8]
            new_df.at[index, 'Frequency'] = data[8:14]
            new_df.at[index, 'ID'] = data[20:]
        else:
            new_df.at[index, 'Data'] = row['Data']
            new_df.at[index, 'QI'] = None
            new_df.at[index, 'Frequency'] = None
            new_df.at[index, 'ID'] = None

    print(new_df.head(10))
    new_df.to_csv('../src/extracted_data.csv', index=False)


def rssi_to_dec():
    df = pd.read_csv('../data/rssi.csv')
    # print(df.head(10))
    new_df = pd.DataFrame(columns=['RSSI Dec'])
    df['RSSI Hex'] = df['RSSI Hex'].fillna(0)
    df['RSSI Hex'] = df['RSSI Hex'].astype('str')

    # print(df.dtypes)
    for index, row in df.iterrows():
        new_df.at[index, 'RSSI Dec'] = int(row['RSSI Hex'], 16)
    new_df.to_csv('../src/converted_rssi.csv', index=False)


if __name__ == '__main__':
    # barr = b'\x44\x05\x00\x00\x00'
    # write_result(barr, datetime.now())
    # extract_data()
    rssi_to_dec()
