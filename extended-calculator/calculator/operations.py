def add(*args):
    # Using helper from Python's core utils
    # Gotta love those, it would've been possible
    # with a for loop either way.
    return sum(args)

def subtract(*args):
    # We subtract from this
    minuend = args[0]
    # All the values found in here
    subtrahend = args[1:]
    # For each value found in subtrahend
    # We subtract it from the minuend which most of the time
    # is supposed to be a bigger number than the rest.
    for taken in subtrahend:
        minuend -= taken

    return minuend

def multiply(*args):
    # We need a starter positive unit so We declare a variable with the number
    # one as a starter, so we take it from there
    multiplicand = 1
    # Iterate through the arguments, multiplying each other in order until done
    for multipliers in args:
        multiplicand *= multipliers
    # Return the multiplicand final value.
    return multiplicand


def divide(*args):
    # your implementation here
    pass

def plot(*args):
    # OPTIONAL EXTRA CREDIT FUNCTION! 
    # See README for info.
    pass

# add your custom operations here
