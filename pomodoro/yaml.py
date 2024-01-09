from dateutil import parser as date_parser
from datetime import timedelta

def generateYAML(duration, timeList, name):
    yaml_content = ''

    yaml_content = yaml_content + 'alias: "Pomodoro - ' + name + ' (' + str(duration) + ' mins)' + '"\n'
    yaml_content = yaml_content + 'description: "' + name + ' for ' + str(duration) + ' mins"\n'
    yaml_content = yaml_content + 'trigger:\n'

    for time in timeList:
        yaml_content = yaml_content + '  - platform: time\n'
        yaml_content = yaml_content + '    at: "' + time.strftime('%H:%M') + '"\n'

    yaml_content = yaml_content + '# Insert conditions and actions here\n'

    return yaml_content

def outputYAML(duration, working_hours, short_break, short_breaks, long_break, long_breaks):
    with open('pomodoro-work.yaml', 'w') as yaml_file:
        yaml_file.write(generateYAML(duration, working_hours, "work"))

    with open('pomodoro-short-break.yaml', 'w') as yaml_file:
        yaml_file.write(generateYAML(short_break, short_breaks, "short break"))

    with open('pomodoro-long-break.yaml', 'w') as yaml_file:
        yaml_file.write(generateYAML(long_break, long_breaks, "long break"))

    print('\nHomeAssistant automation yaml files created')
