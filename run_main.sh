#!/bin/bash

# Follow the instructions here:
# https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line
# to generate your own token. Copy and paste your generated token **inside** the quotation marks below.
MY_TOKEN=""

[[ $# -gt 1 ]] && echo "Warning: only 1 argument <your_username> required. Only the first argument will be considered."

# No need to check if [ -z $MY_TOKEN ]
# if MY_TOKEN is empty, then, when it's passed on to the Python script, it will not be detected as an argument.
python3 main.py $1 $MY_TOKEN
