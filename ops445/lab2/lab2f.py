#!/usr/bin/env python3
# Author: Sithum Kavmal Bamunuarachchi
# Author ID: Sbamunuarachchi
# Date Created: 2024/01/22

import sys

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <count>")
    sys.exit(1)

# Assign command-line argument to the variable timer
timer = int(sys.argv[1])

# While loop to countdown
while timer > 0:
    print(timer)
    timer -= 1

# Print "blast off!"
print("blast off!")