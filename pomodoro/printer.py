from dateutil import parser as date_parser
from datetime import timedelta

def printHours(working_hours, short_breaks, long_breaks):
    print('\nWorking hours:')
    for time in working_hours:
        print(time.strftime('%H:%M'))

    print('\nShort breaks:')
    for time in short_breaks:
        print(time.strftime('%H:%M'))

    print('\nLong breaks:')
    for time in long_breaks:
        print(time.strftime('%H:%M'))
