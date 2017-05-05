def what_is_this(param):
    # The script follows this logical order because
    # any variable with a value is True
    if isinstance(param, float):
        return 'This is a Float.'
    elif isinstance(param, bool):
        return 'This is a Boolean.'
    elif isinstance(param, int):
        return 'This is an Integer.'
    elif isinstance(param, str):
        return 'This is a String.'
    else:
        return 'I have no idea what this is'
