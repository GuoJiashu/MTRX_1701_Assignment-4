import serial
import csv
from datetime import datetime

serial_port = 'COM1'
baud_rate = 9600

csv_filename = 'temperature_data.csv'
csv_header = ['Time', 'Voltage Drop']
with open(csv_filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(csv_header)

ser = serial.Serial(serial_port, baud_rate)

while True:
    serial_data = ser.readline().decode().strip()

    if serial_data:
        temperature = float(serial_data)

        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        print(f'Voltage Drop: {temperature} °C')

        with open(csv_filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, temperature])
