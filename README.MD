# System Requirements

Before running the tests, please ensure you have the following installed:

## Required System Packages

- ffmpeg
  - macOS: `brew install ffmpeg`
  - Windows: `choco install ffmpeg`
  - Linux: `sudo apt-get install ffmpeg`

## Python Dependencies

Install Python dependencies using:

```
pip3 install -r requirements.txt
```

```
brew install node

```

```

brew install allure

```

# .env

```

APPIUM_OS="android" # android or ios
IMPLICIT_WAIT=15
NO_RESET="True"
AUTO_ACCEPT_ALERTS="True"
UDID="4BEC1422-4429-4EAD-B850-C296B013A210" #Optional

```

# How to run allure report (Primary use)

```

pytest --alluredir=./allure-results

```

# Run failed tests and update allure report

```

pytest --lf --alluredir=./allure-results --reruns 3

```

# How to generate allure report

```

allure generate allure-results -o allure-report --clean

```

or

```

allure serve allure-results

```

```

```
