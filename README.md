<div align="center">
  <img src="assets/unitasker_logo.png" alt="Example Image" width="300">
</div>

# Unitasker
A collection of Python functions or scripts for unit conversion. They are bespoke and added as created, so they are not necessarily consistent in naming or formatting. Hopefully they are clear to use. 

## generalPurpose.py

#### `length_conversion(value, from_unit, to_unit)`
Converts a length value between units such as meters, kilometers, inches, and feet.

#### `mass_conversion(value, from_unit, to_unit)`
Converts a mass value between units such as kilograms, grams, pounds, and ounces.

#### `pressure_conversion(value, from_unit, to_unit)`
Converts a pressure value between units such as pascals, bar, psi, and atm.

#### `temperature_conversion(value, from_unit, to_unit)`
Converts a temperature value between Celsius, Fahrenheit, and Kelvin.

#### `volume_conversion(value, from_unit, to_unit)`
Converts a volume value between units such as liters, cubic meters, cubic inches, and cubic feet.

### Example Usage

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
```

## Imperial Fraction to Millimeters Conversion

This Python function converts diameter and thickness measurements from imperial fractions to millimeters.

#### `imperial_fraction_to_mm(diameter_fraction, thickness_fraction)`
Converts diameter and thickness from imperial fractions to millimeters.

#### Args:
- `diameter_fraction (str)`: Diameter as an imperial fraction (e.g., "1 1/2").
- `thickness_fraction (str)`: Thickness as an imperial fraction (e.g., "3/4").

#### Returns:
- `tuple`: Diameter and thickness in millimeters.

### Example Usage

```python
# Example usage
diameter = "1 3/8"  # Example diameter in imperial fraction
thickness = "3/8"   # Example thickness in imperial fraction
diameter_mm, thickness_mm = imperial_fraction_to_mm(diameter, thickness)

print(f"Diameter: {diameter_mm:.2f} mm")
print(f"Thickness: {thickness_mm:.2f} mm")
```
## pa_to_inHg.py
A function to convert Pascals to inches of Mercury. I don't use this often but is handy.

### Usage

```python

pressureHg = pascal_to_inches_of_mercury(101325)
```
