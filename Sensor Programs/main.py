# import get_MQ_voltages from gas_test and get_bme280_data from test_atm
from test_atm import get_bme280_data
from gas_test import get_MQ_voltages
# Configuration

# try printing the readings from both sensors
mq4_voltage, mq135_voltage = get_MQ_voltages()
temp_c, humidity, timestamp_tz = get_bme280_data()

print(timestamp_tz.strftime('%H:%M:%S %d/%m/%Y') + " Temp={0:0.1f}ºC, Temp={1:0.1f}ºF, Humidity={2:0.1f}%".format(temperature_celsius, temperature_fahrenheit, humidity))
print(f"MQ4 Voltage: {mq4_voltage:.3f} V")
print(f"MQ135 Voltage: {mq135_voltage:.3f} V")
