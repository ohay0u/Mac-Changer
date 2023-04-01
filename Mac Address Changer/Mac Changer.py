#!/usr/bin/env python3

import subprocess
import optparse
import re

def mac_changer():
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", macc])
    subprocess.call(["ifconfig", interface, "up"])
    print("")
    print("* Changing " + interface + " Mac Address to " + macc + " *")
    print("")


analizi = optparse.OptionParser()
analizi.add_option("-i", "--interface", dest="Interface", help="Optional Interface")
analizi.add_option("-m", "--mac", dest="Mac Address", help="New Mac Address")
analizi.parse_args()


print("[+] Hello this is Mac Changer, Please enter info")
print("")
print("[!] Warning: First octet of Mac should be even number!")

print("")

interface = input("Enter Interface: ")
macc = input("Enter new Mac: ")

if interface == "wlan0":
    mac_changer()
elif interface == "eth0":
    mac_changer()
else:
    print("")
    print("[!] Enter right interface")

ifconfig = subprocess.check_output(["ifconfig", interface])

ifconfig_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig))
print("ifconfig result > " + ifconfig_result.group(0))