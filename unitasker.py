INCH_TO_MM = 25.4

def pressure_conversion(value: float, from_unit: str, to_unit: str) -> float:
    """
    Convert pressure between different units.

    Args:
        value (float): The pressure value to convert.
        from_unit (str): The current unit of the value.
        to_unit (str): The unit to convert to.

    Returns:
        float: Pressure in the desired unit.
    """
    conversions = {
        'pascal': 1.0,
        'kilopascal': 1000.0,
        'megapascal': 1_000_000.0,
        'bar': 100_000.0,
        'psi': 6894.76,
        'atm': 101_325.0
    }
    if from_unit not in conversions or to_unit not in conversions:
        raise ValueError(f"Units must be one of {list(conversions.keys())}")
    return value * conversions[from_unit] / conversions[to_unit]

def pascal_to_inches_of_mercury(pascals: float) -> float:
    """
    Convert pascals to inches of mercury.

    Args:
        pascals (float): Pressure in pascals.

    Returns:
        float: Pressure in inches of mercury.
    """
    return pascals * 0.0002953

def convert_fraction(fraction: str) -> float:
    """
    Convert an imperial fraction in string format to a float (in inches).

    Args:
        fraction (str): e.g., "1 1/2" or "3/4"

    Returns:
        float: Value in inches.
    """
    if ' ' in fraction:
        whole, frac = fraction.split()
        whole = int(whole)
        num, denom = map(int, frac.split('/'))
        return whole + num / denom
    elif '/' in fraction:
        num, denom = map(int, fraction.split('/'))
        return num / denom
    else:
        return float(fraction)

def imperial_fraction_to_mm(diameter_fraction: str, thickness_fraction: str) -> tuple[float, float]:
    """
    Convert diameter and thickness from imperial fractions to millimeters.

    Args:
        diameter_fraction (str)
        thickness_fraction (str)

    Returns:
        tuple: (diameter_mm, thickness_mm)
    """
    diameter_in_inches = convert_fraction(diameter_fraction)
    thickness_in_inches = convert_fraction(thickness_fraction)
    diameter_in_mm = diameter_in_inches * INCH_TO_MM
    thickness_in_mm = thickness_in_inches * INCH_TO_MM
    return diameter_in_mm, thickness_in_mm

# Example usage
diameter = "1 3/8"
thickness = "3/8"
diameter_mm, thickness_mm = imperial_fraction_to_mm(diameter, thickness)
print(f"Diameter: {diameter_mm:.2f} mm")
print(f"Thickness: {thickness_mm:.2f} mm")