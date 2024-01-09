# Home Assistant Pomodoro YAML Generator

A small and simple Python 3 script to generate the `alias`, `description`, and `trigger` parts of 3 separate YAML files:

    - `pomodoro-long-break.yaml`
    - `pomodoro-short-break.yaml`
    - `pomodoro-work.yaml`

You can then add the generated YAML to the beginning of your automation(s) using the HomeAssistant Web UI.

## Usage

```bash
python3 pomodoro.py [-h] [-d DURATION] [-s SHORT] [-l LONG] [-t TOTAL] [-b BEGINNING] [-v VERBOSE]
```

### Optional arguments

|Option|Description|
|---|---|
`-h, --help` | show this help message and exit
`-d DURATION, --duration DURATION` |Work duration in minutes
`-s SHORT, --short SHORT` | Short break duration in minutes
`-l LONG, --long LONG` |Long break duration in minutes
`-t TOTAL, --total TOTAL`|Total work duration in hours
`-b BEGINNING, --beginning BEGINNING`|Beginning time (HH:MM - military time)
`-v VERBOSE, --verbose VERBOSE`|Output more info

## Example

### Input

```bash
python3 pomodoro.py -d 25 -s 5 -l 30 -t 8 -b 11:00 -v
```

### Output

#### Command output

```text
Pomodoro automation YAML generator v0.1.0
by @recoskyler - 2024
---------------------------------

Duration: 25
Short break: 5
Long break: 30
Total: 8
Beginning: 11:00


Working hours:
11:00
11:30
12:00
12:30
13:25
13:55
14:25
14:55
15:50
16:20
16:50
17:20
18:15
18:45

Short breaks:
11:25
11:55
12:25
13:50
14:20
14:50
16:15
16:45
17:15
18:40
19:10

Long breaks:
12:55
15:20
17:45

HomeAssistant automation yaml files created
```

#### Files

##### `pomodoro-long-break.yaml`

```yaml
alias: "Pomodoro - long break (30 mins)"
description: "long break for 30 mins"
trigger:
  - platform: time
    at: "12:55"
  - platform: time
    at: "15:20"
  - platform: time
    at: "17:45"
# Insert conditions and actions here
```

##### `pomodoro-short-break.yaml`

```yaml
alias: "Pomodoro - short break (5 mins)"
description: "short break for 5 mins"
trigger:
  - platform: time
    at: "11:25"
  - platform: time
    at: "11:55"
  - platform: time
    at: "12:25"
  - platform: time
    at: "13:50"
  - platform: time
    at: "14:20"
  - platform: time
    at: "14:50"
  - platform: time
    at: "16:15"
  - platform: time
    at: "16:45"
  - platform: time
    at: "17:15"
  - platform: time
    at: "18:40"
  - platform: time
    at: "19:10"
# Insert conditions and actions here
```

##### `pomodoro-work.yaml`

```yaml
alias: "Pomodoro - work (25 mins)"
description: "work for 25 mins"
trigger:
  - platform: time
    at: "11:00"
  - platform: time
    at: "11:30"
  - platform: time
    at: "12:00"
  - platform: time
    at: "12:30"
  - platform: time
    at: "13:25"
  - platform: time
    at: "13:55"
  - platform: time
    at: "14:25"
  - platform: time
    at: "14:55"
  - platform: time
    at: "15:50"
  - platform: time
    at: "16:20"
  - platform: time
    at: "16:50"
  - platform: time
    at: "17:20"
  - platform: time
    at: "18:15"
  - platform: time
    at: "18:45"
# Insert conditions and actions here
```

## Development

1. Just clone the [repository](https://github.com/recoskyler/home-assistant-pomodoro.git):

    ```bash
    git clone https://github.com/recoskyler/home-assistant-pomodoro.git
    ```

2. Open the folder in your favorite editor.

## [License](https://github.com/recoskyler/home-assistant-pomodoro/blob/main/LICENSE)

## About

Made by [recoskyler](https://github.com/recoskyler) - 2024
