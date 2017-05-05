def string2number(a_string):
    # Must find out a better way to do this sort of check
    if isinstance(a_string, bool):
        raise ValueError('No booleans allowed')

    if type(float(a_string)) is float or int:
        if a_string.count('.') != 1:
            return int(a_string)
        else:
            return float(a_string)

    if isinstance(a_string, str):
        raise ValueError('No strings allowed')
