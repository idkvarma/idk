import subprocess
import sys
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
    up_count = 0
    down_count = 0

    for i in range(1, 25):
        ip = network_prefix + str(i)
        status = check_system_status(ip)
        if status:
            sys.stdout.write(colored(f"{ip} is up", 'green') + ' | ')
            up_count += 1
        else:
            sys.stdout.write(colored(f"{ip} is down", 'red') + ' | ')
            down_count += 1

        if i % 6 == 0:
            sys.stdout.write("\n")  # Add a newline after every 6 IP addresses

    sys.stdout.write("\n")  # Add a newline after displaying all systems

    print(f"Total systems: {up_count + down_count}")
    print(f"Systems up: {up_count}")
    print(f"Systems down: {down_count}")

if __name__ == "__main__":
    main()

