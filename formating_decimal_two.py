def two_decimal_places(number):
    a = str(number).split('.')
    return float(f'{a[0]}.{a[1][:2]}')