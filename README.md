# Unitasker
A collection of Python functions or scripts for unit conversion

## Pressure.Py

### `length_conversion(value, from_unit, to_unit)`
Converts a length value between units such as meters, kilometers, inches, and feet.

### `mass_conversion(value, from_unit, to_unit)`
Converts a mass value between units such as kilograms, grams, pounds, and ounces.

### `pressure_conversion(value, from_unit, to_unit)`
Converts a pressure value between units such as pascals, bar, psi, and atm.

### `temperature_conversion(value, from_unit, to_unit)`
Converts a temperature value between Celsius, Fahrenheit, and Kelvin.

### `volume_conversion(value, from_unit, to_unit)`
Converts a volume value between units such as liters, cubic meters, cubic inches, and cubic feet.

## Usage

To use these functions, import the script and call the desired function with the appropriate parameters.

```python
# Example usage
length_in_meters = length_conversion(100, 'meters', 'feet')
mass_in_pounds = mass_conversion(5, 'kilograms', 'pounds')
pressure_in_psi = pressure_conversion(101325, 'pascals', 'psi')
temperature_in_fahrenheit = temperature_conversion(0, 'celsius', 'fahrenheit')
volume_in_cubic_inches = volume_conversion(2, 'liters', 'cubic_inches')

print(f"Length: {length_in_meters} feet")
print(f"Mass: {mass_in_pounds} pounds")
print(f"Pressure: {pressure_in_psi} psi")
print(f"Temperature: {temperature_in_fahrenheit} Fahrenheit")
print(f"Volume: {volume_in_cubic_inches} cubic inches")

