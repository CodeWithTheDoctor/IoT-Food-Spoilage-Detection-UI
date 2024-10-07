import smbus2
import bme280
import pytz

def get_bme280_data(address=0x76):
    """
    Reads BME280 sensor data and returns temperature and humidity.

    Parameters:
    address (int): I2C address of the BME280 sensor.

    Returns:
    tuple: (temperature_celsius, humidity, timestamp)
    """
    try:
        # Use 'with' to ensure the bus is closed after reading
        with smbus2.SMBus(1) as bus:
            # Load calibration parameters
            calibration_params = bme280.load_calibration_params(bus, address)

            # Read sensor data
            data = bme280.sample(bus, address, calibration_params)

            # Extract temperature, pressure, humidity, and corresponding timestamp
            temperature_celsius = data.temperature
            humidity = data.humidity
            timestamp = data.timestamp

            # Adjust timezone
            timezone = 'Australia/Perth'
            desired_timezone = pytz.timezone(timezone)
            timestamp_tz = timestamp.replace(tzinfo=pytz.utc).astimezone(desired_timezone)

            return temperature_celsius, humidity, timestamp_tz

    except Exception as e:
        print('An unexpected error occurred:', str(e))
        return None, None, None
