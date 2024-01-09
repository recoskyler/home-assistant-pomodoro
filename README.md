# Home Assistant Pomodoro YAML Generator

A small and simple Python 3 script to generate the `alias`, `description`, and `trigger` parts of 3 separate YAML files:

    - `pomodoro-long-break.yaml`
    - `pomodoro-short-break.yaml`
    - `pomodoro-work.yaml`

You can then add the generated YAML to the beginning of your automation(s) using the HomeAssistant Web UI.

## Usage

```bash
pomodoro.py [-h] [-d DURATION] [-s SHORT] [-l LONG] [-t TOTAL] [-b BEGINNING] [-v VERBOSE]
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

## Development

1. Just clone the [repository](https://github.com/recoskyler/home-assistant-pomodoro.git):

    ```bash
    git clone https://github.com/recoskyler/home-assistant-pomodoro.git
    ```

2. Open the folder in your favorite editor.

## [License](https://github.com/recoskyler/home-assistant-pomodoro/blob/main/LICENSE)

## About

Made by [recoskyler](https://github.com/recoskyler) - 2024
