"""
Generate and output YAML files for HomeAssistant automation.
"""

def generate_yaml(duration, time_list, name):
    """
    The function `generate_yaml` generates YAML content for a Pomodoro timer with
    a specified duration, time list, and name.

    :param duration: The duration parameter represents the length of time
    for the Pomodoro session in minutes
    :param time_list: A list of datetime objects representing the specific
    times at which the trigger should occur
    :param name: The name parameter is a string that represents the name of the Pomodoro session
    :return: a YAML content string.
    """

    yaml_content = ''

    yaml_content = yaml_content + 'alias: "Pomodoro - ' + name + ' (' + str(duration) + ' mins)' + '"\n'
    yaml_content = yaml_content + 'description: "' + name + ' for ' + str(duration) + ' mins"\n'
    yaml_content = yaml_content + 'trigger:\n'

    for time in time_list:
        yaml_content = yaml_content + '  - platform: time\n'
        yaml_content = yaml_content + '    at: "' + time.strftime('%H:%M:%S') + '"\n'

    yaml_content = yaml_content + '# Insert conditions and actions here\n'

    return yaml_content

def output_yaml(duration, working_hours, short_break, short_breaks, long_break, long_breaks):
    """
    The function `outputYAML` creates YAML files for HomeAssistant automation based on the given
    parameters.

    :param duration: The duration parameter represents the length of time for each work session in
    minutes
    :param working_hours: The `working_hours` parameter represents the duration of the work period in
    minutes
    :param short_break: The parameter "short_break" represents the duration of each short break during a
    pomodoro session
    :param short_breaks: The parameter "short_breaks" refers to the number of short breaks you want to
    include in your Pomodoro timer
    :param long_break: The parameter "long_break" represents the duration of a long break in minutes
    :param long_breaks: The parameter "long_breaks" refers to the number of long breaks you want to
    include in your Pomodoro timer
    """

    with open('pomodoro-work.yaml', 'w', encoding='utf8') as yaml_file:
        yaml_file.write(generate_yaml(duration, working_hours, "work"))

    with open('pomodoro-short-break.yaml', 'w', encoding='utf8') as yaml_file:
        yaml_file.write(generate_yaml(short_break, short_breaks, "short break"))

    with open('pomodoro-long-break.yaml', 'w', encoding='utf8') as yaml_file:
        yaml_file.write(generate_yaml(long_break, long_breaks, "long break"))

    print('\nHomeAssistant automation yaml files created')
