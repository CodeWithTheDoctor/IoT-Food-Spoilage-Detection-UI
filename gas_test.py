from ExpanderPi import ADC
import time

# Initialize the ADC module
adc = ADC()

# MQ4 and MQ135 sensors connected ADC channels
mq4_channel = 1  # Replace with the ADC channel connected to MQ4 A0 pin
mq135_channel = 2  # Replace with the ADC channel connected to MQ135 A0 pin

# If using an external reference voltage, set the reference voltage (optional)
# adc.set_adc_refvoltage(4.096)

try:
    while True:
        # Read the voltage from the MQ4 sensor (single-ended mode)
        mq4_voltage = adc.read_adc_voltage(mq4_channel, 0)  # 0 means single-ended mode
        # Read the voltage from the MQ135 sensor (single-ended mode)
        mq135_voltage = adc.read_adc_voltage(mq135_channel, 0)

        # Print the voltage readings
        print(f"MQ4 Voltage: {mq4_voltage:.3f} V")
        print(f"MQ135 Voltage: {mq135_voltage:.3f} V")

        # Read every second
        time.sleep(5)

except KeyboardInterrupt:
    print("Program terminated")
