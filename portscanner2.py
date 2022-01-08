#!/usr/bin/python3

import socket
import pyfiglet
import sys
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

if len(sys.argv) == 2:
   # Translate hostname to IPV4
   target = socket.gethostbyname(sys.argv[1])
else:
   print("Invalid amount of Argument")
   print("Usage: python3 portscanner2.py [URL]")

print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at: " + str(datetime.now()))

try:
   for port in range(1,255):
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      socket.setdefaulttimeout(1)

      result = s.connect_ex((target,port))
      if result == 0:
          print("Port {} is Open".format(port))
      s.close()

except keyboardInterrupt:
    print("\n Exiting Program !!!")
    sys.exit()

except socket.gaierror:
    print("\n Hostname could not be resolved !!!")
    sys.exit()

except socket.error:
    print("\n Server not responding !!!")
    sys.exit()
