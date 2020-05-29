#!/bin/bash

# Follow the instructions here:
# https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line
# to generate your own token. Replace the text between the quotation marks with your generated token.
MY_TOKEN='copy_and_paste_your_generated_token_here'

python main.py $1 $MY_TOKEN
