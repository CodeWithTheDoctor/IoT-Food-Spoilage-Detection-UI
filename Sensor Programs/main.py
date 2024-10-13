import firebase_admin
from firebase_admin import credentials, firestore
from test_atm import get_bme280_data
from gas_test import get_MQ_voltages
import time
import os
import psutil  # To check system resources

# Define the experiment name - This will also be the name of the document on Firestore
EXPERIMENT_NAME = 'Rice2'

def report_sensor_data():
    cred = credentials.Certificate("../serviceAccountKey.json")  # Replace with the path to your service account key
    firebase_admin.initialize_app(cred)
    db = firestore.client()

    # Get the system's maximum allowed open files
    max_open_files = os.sysconf('SC_OPEN_MAX')

    # Monitor resources to avoid overloading the Raspberry Pi
    def check_system_resources():
        mem = psutil.virtual_memory()
        open_files = len(psutil.Process(os.getpid()).open_files())
        
        if mem.percent > 90:
            print("Warning: Memory usage is high.")
        if open_files >= max_open_files * 0.9:
            print(f"Warning: Too many open files ({open_files}/{max_open_files}).")
        return mem.percent, open_files

    # Reference to the experiment document in the Experiment collection
    experiment_ref = db.collection('Experiment').document(EXPERIMENT_NAME)

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

            # Check if the experiment document exists
            if not experiment_ref.get().exists:
                # Create the experiment document with createdAt and name fields
                experiment_ref.set({
                    "createdAt": firestore.SERVER_TIMESTAMP,
                    "name": "rice",
                    "readings": []
                })
                print(f"{EXPERIMENT_NAME} document created.")

            # Append the new sensor data to the readings array
            experiment_ref.update({
                'readings': firestore.ArrayUnion([sensor_data])
            })

            # Print the readings
            print(f"Temp={temp_c:0.1f}ºC, Humidity={humidity:0.1f}%")
            print(f"MQ4 Voltage: {mq4_voltage:.3f} V")
            print(f"MQ135 Voltage: {mq135_voltage:.3f} V")

            # Wait for 1 minute before the next reading
            time.sleep(60)

        except KeyboardInterrupt:
            print("Program terminated")
            break
        except Exception as e:
            print("An error occurred:", str(e))
            time.sleep(5)

# Start reporting sensor data
report_sensor_data()
