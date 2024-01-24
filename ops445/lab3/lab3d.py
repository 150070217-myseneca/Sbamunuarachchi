# Author ID: Sbamunuarachchi

#!/usr/bin/env python3

"""
Author ID: [seneca_id]
"""

import subprocess

def free_space():
    try:
        # Launch the Linux command: df -h | grep '/$' | awk '{print $4}' as a new process
        result = subprocess.run(['df', '-h', '|', 'grep', '/$', '|', 'awk', '{print $4}'], 
                                capture_output=True, text=True, check=True)

        # Return the free disk space as a string with newline characters stripped
        return result.stdout.strip()

    except subprocess.CalledProcessError as e:
        # Handle any errors that may occur during the process execution
        return f"Error: {e}"

if __name__ == '__main__':
    # If the script is run directly, print the result of free_space() function
    print(free_space())

