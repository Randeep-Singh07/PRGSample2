def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

c = float(input("Enter temperature in Degree Celsius: "))
print(f"The temperature is equivalent to {celsius_to_fahrenheit(c):.1f} Fahrenheit")
