def truncatechars(text, truncate_after):
    # If it's not a string, throw error
    if not isinstance(text, (str)):
        raise ValueError
    else:
        # If the value of truncate_after is greater than the
        # length of the text variable, return input as it is.
        if truncate_after > len(text):
            return text
        # Truncate the string after n (truncate_after) and append
        # those three dots at the end.
        else:
            return text[:truncate_after] + '...'
