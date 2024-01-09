def parseArgs():
    parser = argparse.ArgumentParser(description='Generate HomeAssistant automations for Pomodoro')

    parser.add_argument('-d', '--duration', help='Work duration in minutes', type=int, default=25)
    parser.add_argument('-s', '--short', help='Short break duration in minutes', type=int, default=5)
    parser.add_argument('-l', '--long', help='Long break duration in minutes', type=int, default=30)
    parser.add_argument('-t', '--total', help='Total work duration in hours', type=int, default=8)
    parser.add_argument('-b', '--beginning', help='Beginning time (HH:MM - military time)', type=str, default='11:00')
    parser.add_argument('-v', '--verbose', help='Output more info', type=str, default=False)

    return parser.parse_args()

def main():
    print('Pomodoro automation YAML generator v0.1.0')
    print('by @recoskyler - 2024')
    print('---------------------------------\n')

    args = parseArgs()

    # Set variables

    duration = args.duration
    short_break = args.short
    long_break = args.long
    total = args.total
    verbose = args.verbose
    beginning = date_parser.parse(args.beginning)

    # Generate working hours

    hours = calculateHours(duration, short_break, long_break, total, beginning)

    working_hours = hours[0]
    short_breaks = hours[1]
    long_breaks = hours[2]

    # Print out times

    if verbose:
        printHours(working_hours, short_breaks, long_breaks)

    outputYAML(duration, working_hours, short_break, short_breaks, long_break, long_breaks)

if __name__ == '__main__':
    import argparse
    from dateutil import parser as date_parser
    from datetime import timedelta
    from pomodoro.calculator import calculateHours
    from pomodoro.yaml import outputYAML
    from pomodoro.printer import printHours

    main()
