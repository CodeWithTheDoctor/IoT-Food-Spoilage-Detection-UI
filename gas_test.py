from expanderpi import ADC
import time

# Initialize the ADC module
adc = ADC()

# Define the ADC channels connected to MQ4 and MQ135
mq4_channel = 1  # Replace with the ADC channel connected to the MQ4 A0 pin
mq135_channel = 2  # Replace with the ADC channel connected to the MQ135 A0 pin

try:
    while True:
        # Read the analog value from the MQ4 sensor
        mq4_value = adc.read_adc(mq4_channel, 12)  # Read with 12-bit resolution
        # Read the analog value from the MQ135 sensor
        mq135_value = adc.read_adc(mq135_channel, 12)
        
        # Print the sensor readings
        print(f"MQ4 Analog Value: {mq4_value}")
        print(f"MQ135 Analog Value: {mq135_value}")
        
        # Read every second
        time.sleep(1)

except KeyboardInterrupt:
    print("Program terminated")