"""
Prints the calculated hours.
"""

def print_hours(working_hours, short_breaks, long_breaks):
    """
    Prints the calculated hours.
    """

    print('\nWorking hours:')
    for time in working_hours:
        print(time.strftime('%H:%M'))

    print('\nShort breaks:')
    for time in short_breaks:
        print(time.strftime('%H:%M'))

    print('\nLong breaks:')
    for time in long_breaks:
        print(time.strftime('%H:%M'))
