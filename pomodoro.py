"""Generates YAML for HomeAssistant automations for Pomodoro.

Returns:
    _type_: _description_
"""

from argparse import ArgumentParser
from dateutil import parser as date_parser
from pomodoro.calculator import calculate_hours
from pomodoro.yaml import output_yaml
from pomodoro.printer import print_hours, print_human_readable_hours

def parse_args():
    """
    The `parse_args()` function is used to parse command line arguments for generating HomeAssistant
    automations for Pomodoro.
    :return: The function `parse_args()` returns the parsed command-line arguments as an
    `argparse.Namespace` object.
    """

    parser = ArgumentParser(description='Generate HomeAssistant automations for Pomodoro')

    parser.add_argument(
        '-d',
        '--duration',
        help='Work duration in minutes',
        type=int,
        default=25
    )
    parser.add_argument(
        '-s',
        '--short',
        help='Short break duration in minutes',
        type=int,
        default=5
    )
    parser.add_argument(
        '-l',
        '--long',
        help='Long break duration in minutes',
        type=int,
        default=30
    )
    parser.add_argument(
        '-t',
        '--total',
        help='Total work duration in hours',
        type=int,
        default=8
    )
    parser.add_argument(
        '-b',
        '--beginning',
        help='Beginning time (HH:MM - military time)',
        type=str,
        default='11:00'
    )
    parser.add_argument(
        '-v',
        '--verbose',
        help='Output more info',
        action='store_true',
    )

    return parser.parse_args()

def main():
    """
    The main function is the entry point of the program.
    """

    print('Pomodoro automation YAML generator v0.1.0')
    print('by @recoskyler - 2024')
    print('---------------------------------\n')

    args = parse_args()

    # Set variables

    duration = args.duration
    short_break = args.short
    long_break = args.long
    total = args.total
    verbose = args.verbose
    beginning = date_parser.parse(args.beginning)

    # Print out variables

    if verbose:
        print('Duration: ' + str(duration))
        print('Short break: ' + str(short_break))
        print('Long break: ' + str(long_break))
        print('Total: ' + str(total))
        print('Beginning: ' + beginning.strftime('%H:%M'))
        print('')

    # Generate working hours

    hours = calculate_hours(duration, short_break, long_break, total, beginning)

    working_hours = hours[0]
    short_breaks = hours[1]
    long_breaks = hours[2]

    # Print out times

    if verbose:
        print_hours(working_hours, short_breaks, long_breaks)
        print_human_readable_hours(working_hours, short_breaks, long_breaks)

    output_yaml(duration, working_hours, short_break, short_breaks, long_break, long_breaks)

if __name__ == '__main__':
    main()
