FROM python:3.11.8

COPY requirements.txt /temp/
# Install any needed packages specified in requirements.txt
RUN pip3 install --no-cache-dir -r /temp/requirements.txt

# Define build-time variables
ARG APPIUM_OS
ARG IMPLICIT_WAIT
ARG NO_RESET
ARG AUTO_ACCEPT_ALERTS
ARG UDID

# Set environment variables
ENV APPIUM_OS=$APPIUM_OS \
    IMPLICIT_WAIT=$IMPLICIT_WAIT \
    NO_RESET=$NO_RESET \
    AUTO_ACCEPT_ALERTS=$AUTO_ACCEPT_ALERTS \
    UDID=$UDID 

# Run app.py when the container launches
CMD ["pytest", "--alluredir=./allure-results"]