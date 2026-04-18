#!/bin/sh

# Gradle Wrapper script for Unix-like systems

# Exit immediately if a command exits with a non-zero status
set -e

# Look for & use the gradle-wrapper.jar file within this project
BASEDIR=$(dirname "$0")

# Determine the OS type
OS=`uname`
if [ "Darwin" = "$OS" ]; then
  GRADLE_WRAPPER_JAR="$BASEDIR/gradle/wrapper/gradle-wrapper.jar"
  exec java -jar "$GRADLE_WRAPPER_JAR" "$@"
elif [ "Linux" = "$OS" ]; then
  GRADLE_WRAPPER_JAR="$BASEDIR/gradle/wrapper/gradle-wrapper.jar"
  exec java -jar "$GRADLE_WRAPPER_JAR" "$@"
else
  echo "Unsupported operating system: $OS"
  exit 1
fi