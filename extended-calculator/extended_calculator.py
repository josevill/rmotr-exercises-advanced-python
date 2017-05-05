from datetime import datetime

from calculator.operations import *
from calculator.exceptions import *

def create_new_calculator(operations=None):
    """
    Creates a configuration dict for a new calculator. Optionally pre loads an
    initial set of operations. By default a calculator with no operations
    is created. Returns a dict containing operations(dict) and history(list).

    :param operations: Dict with initial operations.
                       ie: {'sum': sum_function, ...}
    """
    # Check if there aren't any params, declare them empty.
    if operations is None:
        operations = {}
    # Return calculator with operations and an empty history
    # of operations.
    return {'operations' : operations, 'history' : []}

def are_valid_params(params):
    """
    Check if params given are correct and usable in our script.
    """
    try:
        assert isinstance(params, tuple)
        assert all([isinstance(value, (int, float)) for value in params])
    except AssertionError:
        return False
    return True

def perform_operation(calc, operation, params):
    """
    Executes given operation with given params. It returns the result of the
    operation execution.

    :param calc: A calculator.
    :param operation: String with the operation name. ie: 'add'
    :param params: Tuple containing the list of nums to operate with.
                   ie: (1, 2, 3, 4.5, -2)
    """
    if not are_valid_params(params):
        raise InvalidParams('Given params are invalid.')

    if operation in calc['operations'].keys():
        try:
            # Make calculations and save keep the result
            result = calc['operations'][operation](*params)
            # Append as last entry to the history in calc
            calc['history'].append(
                (datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                 operation,
                 params,
                 result))
            return calc['operations'][operation](*params)
        except:
            raise InvalidParams("Given params are invalid.")
    else:
        raise InvalidOperation('"{}" operation not supported', format(operation))

def add_new_operation(calc, operation):
    """
    Adds given operation to the list of supported operations for given calculator.

    :param calc: A calculator.
    :param operation: Dict with the single operation to be added.
                      ie: {'add': add_function}
    """
    if not isinstance(operation, dict):
        raise InvalidOperation("Given operation is invalid.")

    for key, value in operation.items():
        calc['operations'][key] = value

def get_operations(calc):
    """
    Returns the list of operation names supported by given calculator.
    """
    return list(calc['operations'].keys())

def get_history(calc):
    """
    Returns the history of the executed operations since the last reset or
    since the calculator creation.

    History items must have the following format:
        (:execution_time, :operation_name, :params, :result)

        ie:
        ('2016-05-20 12:00:00', 'add', (1, 2), 3),
    """
    return calc['history']

def save_in_history(calc, operation, params, result):
    """
    Save operations made into the passed calculator instance.
    """
    calc['history'].append(
        (datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
         operation,
         params,
         result)
    )

def reset_history(calc):
    """
    Resets the calculator history back to an empty list.
    """

    calc['history'] = []

def repeat_last_operation(calc):
    """
    Return passed calculator's last operation result.
    """
    if calc['history']:
        return calc['history'][-1][-1]
    else:
        return None
