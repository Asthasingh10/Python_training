def smart_home_system(temperature, humidity, motion_detected):
    print("🏠 Smart Home Automation Status:\n")

    # Temperature-based fan control
    if temperature > 30:
        print("🌡️  It's hot! Turning the FAN ON.")
    else:
        print("🌡️  Temperature is fine. Turning the FAN OFF.")

    # Humidity-based dehumidifier control
    if humidity > 70:
        print("💧 Humidity is high! Turning the DEHUMIDIFIER ON.")
    else:
        print("💧 Humidity is normal. Turning the DEHUMIDIFIER OFF.")

    # Motion-based light control
    if motion_detected:
        print("🚶 Motion detected! Turning the LIGHTS ON.")
    else:
        print("🚫 No motion detected. Turning the LIGHTS OFF.")

# Example usage
temperature = float(input("Enter temperature (°C): "))
humidity = float(input("Enter humidity (%): "))
motion_input = input("Is motion detected? (yes/no): ").lower()
motion_detected = True if motion_input == "yes" else False

smart_home_system(temperature, humidity, motion_detected)
