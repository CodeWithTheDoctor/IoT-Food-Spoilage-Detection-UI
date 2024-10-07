import firebase_admin
from firebase_admin import credentials, firestore
from test_atm import get_bme280_data
from gas_test import get_MQ_voltages
import time
import os
import psutil  # To check system resources

def report_sensor_data():
    # Initialize Firebase Admin SDK
    cred = credentials.Certificate("serviceAccountKey.json")  # Replace with the path to your service account key
    firebase_admin.initialize_app(cred)

    # Initialize Firestore client
    db = firestore.client()

    # Monitor resources to avoid overloading the Raspberry Pi
    def check_system_resources():
        mem = psutil.virtual_memory()
        open_files = len(psutil.Process(os.getpid()).open_files())
        max_open_files = os.sysconf('SC_OPEN_MAX')
        
        if mem.percent > 90:
            print("Warning: Memory usage is high.")
        if open_files >= max_open_files * 0.9:
            print("Warning: Too many open files. Consider reducing usage.")
        return mem.percent, open_files

    while True:
        try:
            # Check system resources before proceeding
            mem_usage, open_files = check_system_resources()
            if mem_usage > 90 or open_files >= max_open_files * 0.9:
                time.sleep(10)
                continue

            # Get sensor readings
            mq4_voltage, mq135_voltage = get_MQ_voltages()
            temp_c, humidity, timestamp_tz = get_bme280_data()

            if None in (mq4_voltage, mq135_voltage, temp_c, humidity):
                print("Error reading sensors, retrying...")
                time.sleep(5)
                continue

            # Create a dictionary with the data
            sensor_data = {
                "temperature": temp_c,
                "humidity": humidity,
                "mq4_voltage": mq4_voltage,
                "mq135_voltage": mq135_voltage,
                "timestamp": timestamp_tz
            }

            # Send data to the "readings" collection in Firestore
            db.collection('readings').add(sensor_data)

            # Print the readings
            print(f"Temp={temp_c:0.1f}ºC, Humidity={humidity:0.1f}%")
            print(f"MQ4 Voltage: {mq4_voltage:.3f} V")
            print(f"MQ135 Voltage: {mq135_voltage:.3f} V")

            # Wait for 5 seconds before the next reading
            time.sleep(5)

        except KeyboardInterrupt:
            print("Program terminated")
            break
        except Exception as e:
            print("An error occurred:", str(e))
            time.sleep(5)

# Start reporting sensor data
report_sensor_data()
