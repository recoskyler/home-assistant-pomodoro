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

def print_human_readable_hours(working_hours, short_breaks, long_breaks):
    """
    Prints the calculated hours in a human readable format.
    """

    print('\n=================================\n')
    print('\nHuman readable hours:\n')

    all_hours = working_hours + short_breaks + long_breaks
    all_hours.sort()

    pomodoro_count = 0
    state = -1

    for time in all_hours:
        if state == -1: # Initial state => Working
            state = 0
            print(time.strftime('%H:%M') + ' - Start Working XXXXXXXXXXX')
            continue

        if state == 0: # Working => Short break or Long break
            pomodoro_count = pomodoro_count + 1

            if pomodoro_count == 4: # Working => Long break
                state = 1
                pomodoro_count = 0
                print(time.strftime('%H:%M') + ' - Long break ==============')
            else: # Working => Short break
                state = 2
                print(time.strftime('%H:%M') + ' - Short break -------------')

            continue

        if state == 1: # Long break => Working
            state = 0
            print(time.strftime('%H:%M') + ' - Continue Working ||||||||')

            continue

        if state == 2: # Short break => Working
            state = 0
            print(time.strftime('%H:%M') + ' - Continue Working ||||||||')

            continue
