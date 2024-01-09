from dateutil import parser as date_parser
from datetime import timedelta

def calculateHours(duration, short_break, long_break, total, beginning):
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