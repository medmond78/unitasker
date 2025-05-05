def pressure_conversion(value, from_unit, to_unit):
    conversions = {
        'pascals': 1.0,
        'kilopascals': 1000.0,
        'megapascals': 1000000.0,
        'bar': 100000.0,
        'psi': 6894.76,
        'atm': 101325.0
    }
    return value * conversions[from_unit] / conversions[to_unit]
