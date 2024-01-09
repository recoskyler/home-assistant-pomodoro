"""
Calculates the schedule of working hours, short breaks, and long breaks based on the given duration,
short break duration, long break duration, total number of cycles, and starting time.
"""

from datetime import timedelta

def calculate_hours(duration, short_break, long_break, total, beginning):
    """
    The function calculates the schedule of working hours, short breaks, and long breaks based on the
    given duration, short break duration, long break duration, total number of cycles, and starting
    time.

    :param duration: The duration parameter represents the length of each working session in minutes
    :param short_break: The parameter "short_break" represents the duration of a short break in minutes
    :param long_break: The `long_break` parameter represents the duration of a long break in minutes
    :param total: The "total" parameter represents the total number of pomodoros or work cycles you want
    to complete. Each pomodoro consists of a work session followed by a short break, except after every
    fourth pomodoro, there is a long break instead of a short break
    :param beginning: The `beginning` parameter represents the starting time of the working hours. It
    should be a `datetime` object that specifies the date and time when the working hours begin
    :return: a list containing three lists: working_hours, short_breaks, and long_breaks.
    """

    pomodoro_count = 0
    state = -1
    current_time = beginning
    total_minutes = total * 60
    current_total_minutes = 0

    working_hours = []
    short_breaks = []
    long_breaks = []

    while current_total_minutes <= total_minutes:
        if state == -1: # Initial state => Working
            state = 0
            working_hours.append(beginning)
            continue

        if state == 0: # Working => Short break or Long break
            pomodoro_count = pomodoro_count + 1
            current_total_minutes = current_total_minutes + duration
            current_time = current_time + timedelta(minutes=duration)

            if pomodoro_count == 4: # Working => Long break
                state = 1
                pomodoro_count = 0
                long_breaks.append(current_time)
            else: # Working => Short break
                state = 2
                short_breaks.append(current_time)

            continue

        if state == 1: # Long break => Working
            state = 0
            current_total_minutes = current_total_minutes + long_break
            current_time = current_time + timedelta(minutes=long_break)
            working_hours.append(current_time)

            continue

        if state == 2: # Short break => Working
            state = 0
            current_total_minutes = current_total_minutes + short_break
            current_time = current_time + timedelta(minutes=short_break)
            working_hours.append(current_time)

            continue

    return [working_hours, short_breaks, long_breaks]
