import firebase_admin
from firebase_admin import credentials, firestore
from test_atm import get_bme280_data
from gas_test import get_MQ_voltages

# Initialize Firebase Admin SDK
cred = credentials.Certificate("serviceAccountKey.json")  # Replace with the path to your service account key
firebase_admin.initialize_app(cred)

# Initialize Firestore client
db = firestore.client()

# Get sensor readings
mq4_voltage, mq135_voltage = get_MQ_voltages()
temp_c, humidity, timestamp_tz = get_bme280_data()

# Create a dictionary with the data
sensor_data = {
    "timestamp": timestamp_tz,
    "temperature": temp_c,
    "humidity": humidity,
    "mq4_voltage": mq4_voltage,
    "mq135_voltage": mq135_voltage
}

# Send data to the "readings" collection in Firestore
db.collection('readings').add(sensor_data)

# Print the readings
print(timestamp_tz.strftime('%H:%M:%S %d/%m/%Y') + " Temp={0:0.1f}ºC, Humidity={1:0.1f}%".format(temp_c, humidity))
print(f"MQ4 Voltage: {mq4_voltage:.3f} V")
print(f"MQ135 Voltage: {mq135_voltage:.3f} V")
