def imperial_fraction_to_mm(diameter_fraction, thickness_fraction):
    """
    Convert diameter and thickness from imperial fractions to millimeters.

    Args:
        diameter_fraction (str): Diameter as an imperial fraction (e.g., "1 1/2").
        thickness_fraction (str): Thickness as an imperial fraction (e.g., "3/4").

    Returns:
        tuple: Diameter and thickness in millimeters.
    """
    def convert_fraction(fraction):
        # Split whole and fractional parts
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

    # Convert to inches
    diameter_in_inches = convert_fraction(diameter_fraction)
    thickness_in_inches = convert_fraction(thickness_fraction)

    # Convert to millimeters
    diameter_in_mm = diameter_in_inches * 25.4
    thickness_in_mm = thickness_in_inches * 25.4

    return diameter_in_mm, thickness_in_mm

# Example usage
diameter = "1 3/8"  # Example diameter in imperial fraction
thickness = "3/8"   # Example thickness in imperial fraction
diameter_mm, thickness_mm = imperial_fraction_to_mm(diameter, thickness)

print(f"Diameter: {diameter_mm:.2f} mm")
print(f"Thickness: {thickness_mm:.2f} mm")
