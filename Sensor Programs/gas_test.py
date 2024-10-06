from ExpanderPi import ADC

def get_MQ_voltages(mq4_channel=1, mq135_channel=2):
    """
    Reads and returns the voltages from MQ4 and MQ135 sensors.

    Parameters:
    mq4_channel (int): ADC channel connected to MQ4 sensor.
    mq135_channel (int): ADC channel connected to MQ135 sensor.

    Returns:
    tuple: (mq4_voltage, mq135_voltage)
    """
    # Initialize the ADC module
    adc = ADC()

    try:
        # Read the voltage from the MQ4 sensor (single-ended mode)
        mq4_voltage = adc.read_adc_voltage(mq4_channel, 0)  # 0 means single-ended mode
        # Read the voltage from the MQ135 sensor (single-ended mode)
        mq135_voltage = adc.read_adc_voltage(mq135_channel, 0)

        # print(f"MQ4 Voltage: {mq4_voltage:.3f} V")
        # print(f"MQ135 Voltage: {mq135_voltage:.3f} V")
        return mq4_voltage, mq135_voltage

    except Exception as e:
        print("An error occurred:", str(e))
        return None, None

# Example usage:
# mq4_voltage, mq135_voltage = get_MQ_voltages(mq4_channel=1, mq135_channel=2)