import smbus2
import bme280
import pytz

def get_bme280_data(address=0x76, timezone='Europe/Lisbon'):
    """
    Reads BME280 sensor data and returns temperature and humidity.

    Parameters:
    address (int): I2C address of the BME280 sensor.
    timezone (str): Timezone for the timestamps.

    Returns:
    tuple: (temperature_celsius, temperature_fahrenheit, humidity)
    """
    # Initialize I2C bus
    bus = smbus2.SMBus(1)

    # Load calibration parameters
    calibration_params = bme280.load_calibration_params(bus, address)

    try:
        # Read sensor data
        data = bme280.sample(bus, address, calibration_params)

        # Extract temperature, pressure, humidity, and corresponding timestamp
        temperature_celsius = data.temperature
        humidity = data.humidity
        timestamp = data.timestamp

        # Adjust timezone
        desired_timezone = pytz.timezone(timezone)
        timestamp_tz = timestamp.replace(tzinfo=pytz.utc).astimezone(desired_timezone)

        # Convert temperature to Fahrenheit
        temperature_fahrenheit = (temperature_celsius * 9/5) + 32

        # Print the readings
        # print(timestamp_tz.strftime('%H:%M:%S %d/%m/%Y') + " Temp={0:0.1f}ºC, Temp={1:0.1f}ºF, Humidity={2:0.1f}%".format(temperature_celsius, temperature_fahrenheit, humidity))

        return temperature_celsius, temperature_fahrenheit, humidity

    except Exception as e:
        print('An unexpected error occurred:', str(e))
        return None, None, None

# Example usage:
# temp_c, temp_f, humidity = get_bme280_data(address=0x76, timezone='Europe/Lisbon')