#!/usr/bin/env python
import getpass
import sys
import telnetlib

#inputs from user
user = raw_input("Enter remote account: ")
password = getpass.getpass()

#open file with switches IPs
file = open('switchesip')
for line in file:
  print "Backing Up Running Config of " + str(line)
  # getting rid of white spaces
  HOST = line.strip()

  #telnet in switches
  tn = telnetlib.Telnet(HOST)
  tn.read_until("Username: ")
  tn.write(user + "\n")
  if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

  tn.write("terminal length 0\n")
  tn.write("sh run\n")
  tn.write("exit\n")

  readoutput = tn.read_all()
  saveoutput = open("switch" + HOST,"w")
  saveoutput.write(readoutput)
  saveoutput.close()


