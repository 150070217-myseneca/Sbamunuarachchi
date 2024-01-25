#!/usr/bin/env python3
# Author: Sithum Kavmal Bamunuarachchi
# Author ID: 150070217
# Date Created: 2024/01/22

import sys

# Check if the correct number of command-line arguments is provided
if len(sys.argv) == 1:
    # If no argument is provided, set the default value of timer to 3
    timer = 3
elif len(sys.argv) == 2:
    # If one argument is provided, use it as the value for timer
    timer = int(sys.argv[1])
else:
    # If more than one argument is provided, print usage message and exit
    print(f"Usage: {sys.argv[0]} [count]")
    sys.exit(1)

# While loop to countdown
while timer > 0:
    print(timer)
    timer -= 1

# Print "blast off!"
print("blast off!")