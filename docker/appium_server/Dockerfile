# Use an official Node.js runtime as the base image
FROM node:20.16.0
# Set the working directory in the container
WORKDIR /usr/src/app
# Copy the current directory contents into the container at /usr/src/app
COPY . .

USER root

ENV YARN_VERSION=1.22.22

# RUN apt-get -qqy update && \
#     apt dist-upgrade -y && \
#     apt-get -qqy --no-install-recommends install \
#     ca-certificates \
#     curl \
#     gnupg \
#     libgconf-2-4 \
#     libqt5webkit5 \
#     sudo \
#     tzdata \
#     unzip \
#     wget \
#     xvfb \
#     zip \
#     ffmpeg \
#   && rm -rf /var/lib/apt/lists/*

# Install appium
RUN npm install -g appium && \
    appium driver install uiautomator2 && \
    appium driver install xcuitest

# Make port 4723 available to the world outside this container
EXPOSE 4723

# Start appium server
CMD ["appium", "--log --allow-cors"]