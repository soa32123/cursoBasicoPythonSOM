#!/usr/bin/python3.11

import shlex, subprocess

command_line = 'sudo apt-get install sl -y'

args = shlex.split(command_line)

subprocess.call(args)


