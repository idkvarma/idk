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

    down_systems = 0  # Store the count of systems that are down

    for i in range(1, 25):
        ip = network_prefix + str(i)
        status = check_system_status(ip)
        if not status:
            down_systems += 1
            print(colored(f"{ip} is down", 'red'))
            sys.stdout.flush()  # Flush the output buffer to show the status immediately
            time.sleep(1)  # Wait for 1 second between each down system status

    sys.stdout.write("\n")  # Move to the next line after displaying all systems

    if down_systems > 0:
        print(f"Total systems down: {down_systems}")
    else:
        print("All systems are up.")

if __name__ == "__main__":
    main()

