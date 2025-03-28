#!/usr/bin/env python3

import subprocess
import argparse
import signal
import re
import sys
def def_handler(sig, frame):
    print("\n[!] Saliendo...")
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)
def get_arguments():    
    parser = argparse.ArgumentParser("Change MAC adress of an interface")
    parser.add_argument("-i", "--interface", dest="interface", help="Interface to change")
    parser.add_argument("-m", "--mac", dest="mac_address", help="New MAC address")
    return parser.parse_args()

def is_valid_input(interface, mac):
    
    is_valid_interface = re.match(r'^[e][n|t][s|h]\d{1,2}$', interface)
    is_valid_mac = re.match(r'^[a-fA-F0-9]{2}[:]{5}[a-fA-F0-9]{2}$', mac)
    
    return is_valid_interface and is_valid_mac
    
def change_mac_address(interface, mac):
    if is_valid_input(interface, mac):
        subprocess.run(["ifconfig", interface, "down"])
        subprocess.run(["ifconfig", interface, "hw", "ether", mac])
        subprocess.run(["ifconfig", interface, "up"])
    else:
        print("[-] Invalid input")
    
def main():
    args = get_arguments()
    change_mac_address(args.interface, args.mac_address)

if __name__ == "__main__":
    main()