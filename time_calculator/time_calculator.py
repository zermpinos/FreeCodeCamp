"""
This function takes the start time, the time we want to add and the boolean value of the start day as arguments
and gives back the calculated time and day, if asked, as a string, after the addition.
"""

days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def add_time(start_time, addition, starting_day=None):
    # Split the time into hours minutes with respect to the am/pm and assigns them to separate variables
    # Contain 2 strings, the hour and the AM/PM
    start_time_parts = start_time.split(' ')
    # Further splits the start time to hours and minutes
    start_hour, start_min = [int(part) for part in start_time_parts[0].split(':')]
    # Collect the AM/PM
    start_period = start_time_parts[1].upper()

    # Collect addition hour and minute
    addition_parts = addition.split(':')
    addition_hour, addition_min = [int(part) for part in addition_parts]

    # Convert start hour to 24-hour format
    if start_period == 'PM':
        start_hour += 12

    # Add addition hour and minute to start time
    new_min = (start_min + addition_min) % 60
    leftover = (start_min + addition_min) // 60
    new_hour = (start_hour + addition_hour + leftover) % 24
    new_period = 'AM' if new_hour < 12 else 'PM'
    new_hour = new_hour % 12 or 12

    # Find days passed
    days_passed = (start_hour + addition_hour + leftover) // 24

    # Day of week if asked
    if starting_day:
        starting_day = starting_day.lower().capitalize()
        days_modulo = days_passed % 7
        day_index = (days_modulo + days_of_week.index(starting_day)) % 7
        new_day = days_of_week[day_index]
    else:
        new_day = ''

    # Result String
    if days_passed == 0:
        passed = ''
    elif days_passed == 1:
        passed = ' (next day)'
    else:
        passed = f' ({days_passed} days later)'

    if new_day:
        # :02d formatting is to display time with two digits, which is necessary for the hh:mm format.
        return f'{new_hour}:{new_min:02d} {new_period}, {new_day}{passed}'
    else:
        return f'{new_hour}:{new_min:02d} {new_period}{passed}'
