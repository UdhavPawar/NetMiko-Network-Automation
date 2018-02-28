#!/usr/bin/env python
import getpass
import sys
import telnetlib

v = input("How many vlans to add: ")
user = raw_input("Enter remote account: ")
password = getpass.getpass()

for h in range(242,247):
  HOST = "192.168.122." + str(h)
  tn = telnetlib.Telnet(HOST)
  tn.read_until("Username: ")
  tn.write(user + "\n")
  if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")
  tn.write("conf t\n")

  for n in range(2,v+1):
    tn.write("vlan " + str(n) + "\n")
    tn.write("name Python_VLAN_" + str(n) + "\n")
  tn.write("end\n")
  tn.write("sh vlan br\n")
  tn.write("exit\n")

  print tn.read_all()

