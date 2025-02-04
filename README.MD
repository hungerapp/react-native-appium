# install manually

```
brew install node

```

```
pip3 install -r requirements.txt

```

```
brew install allure

```

# .env

```
APPIUM_OS="ios" # android or ios
IMPLICIT_WAIT=15
DUMMY_PASSWORD="testP@ssword"
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
