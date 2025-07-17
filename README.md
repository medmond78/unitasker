<div align="center">
  <img src="assets/unitasker_logo.png" alt="Unitasker Logo" width="300">
</div>

# Unitasker

A collection of Python functions for unit conversion, written to be clear, concise, and consistent. Additions are incremental: naming and formatting now adhere to current best practices. Unit tests are recommended for reliability and further development.

---

## Contents

- <a href="#function-reference" target="_blank" rel="noopener noreferrer" class="text-blue-500 hover:underline">Function Reference</a>
- <a href="#example-usage" target="_blank" rel="noopener noreferrer" class="text-blue-500 hover:underline">Example Usage</a>
- <a href="#testing" target="_blank" rel="noopener noreferrer" class="text-blue-500 hover:underline">Testing</a>
- <a href="#notes" target="_blank" rel="noopener noreferrer" class="text-blue-500 hover:underline">Notes</a>

---

## Function Reference

### `pressure_conversion(value: float, from_unit: str, to_unit: str) -> float`

Converts a pressure value between units: pascal, kilopascal, megapascal, bar, psi, atm.

**Arguments:**
- `value` (`float`): The pressure value to convert.
- `from_unit` (`str`): The unit of the input value.
- `to_unit` (`str`): The desired output unit.

**Returns:**  
- `float`: Pressure in the desired unit.

---

### `pascal_to_inches_of_mercury(pascals: float) -> float`

Converts Pascals to inches of mercury.

**Arguments:**  
- `pascals` (`float`): Pressure in Pascals.

**Returns:**  
- `float`: Pressure in inches of mercury.

---

### `convert_fraction(fraction: str) -> float`

Converts an imperial fraction (e.g., `"1 1/2"`, `"3/4"`) to a float (in inches).

**Arguments:**
- `fraction` (`str`): The fraction to convert (`"1 1/2"`, `"3/4"`, or `"2"`).

**Returns:**
- `float`: Value in inches.

---

### `imperial_fraction_to_mm(diameter_fraction: str, thickness_fraction: str) -> tuple[float, float]`

Converts diameter and thickness from imperial fractions to millimeters.

**Arguments:**
- `diameter_fraction` (`str`): Diameter as an imperial fraction.
- `thickness_fraction` (`str`): Thickness as an imperial fraction.

**Returns:**
- `tuple (float, float)`: `(diameter_mm, thickness_mm)`

---

## Example Usage

```python
from unitasker import (
    pressure_conversion,
    pascal_to_inches_of_mercury,
    convert_fraction,
    imperial_fraction_to_mm,
)

# Pressure conversion
pressure_psi = pressure_conversion(101325, 'pascal', 'psi')
print(f"Pressure: {pressure_psi:.2f} psi")

# Pascals to inches of mercury
pressure_inHg = pascal_to_inches_of_mercury(101325)
print(f"Pressure: {pressure_inHg:.2f} inHg")

# Imperial fraction to mm
diameter = "1 3/8"
thickness = "3/8"
diameter_mm, thickness_mm = imperial_fraction_to_mm(diameter, thickness)
print(f"Diameter: {diameter_mm:.2f} mm")
print(f"Thickness: {thickness_mm:.2f} mm")