import subprocess
import sys
import time
from termcolor import colored

def check_system_status(ip):
    try:
        # Send a single ping packet with a timeout of 1 second
        subprocess.check_output(['ping', '-c', '1', '-W', '1', ip], stderr=subprocess.STDOUT)
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    network_prefix = "192.168.2."

    up_count = 0  # Store the count of systems that are up

    for i in range(11, 25):
        ip = network_prefix + str(i)
        status = check_system_status(ip)
        if status:
            up_count += 1
            print(colored(f"{ip} is up", 'green'))
            sys.stdout.flush()  # Flush the output buffer to show the status immediately
            time.sleep(1)  # Wait for 1 second between each system status

    print(f"\nTotal systems up: {up_count}")

if __name__ == "__main__":
    main()

