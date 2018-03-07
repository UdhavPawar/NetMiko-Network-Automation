#!/usr/bin/env python

from netmiko import ConnectHandler

iosv_l2_s1 = {
    'device_type' : 'cisco_ios',
    'ip' : '192.168.122.242',
    'username' : 'upawar',
    'password' : 'cisco'
}

iosv_l2_s2 = {
    'device_type' : 'cisco_ios',
    'ip' : '192.168.122.243',
    'username' : 'upawar',
    'password' : 'cisco'
}

iosv_l2_s3 = {
    'device_type' : 'cisco_ios',
    'ip' : '192.168.122.244',
    'username' : 'upawar',
    'password' : 'cisco'
}

iosv_l2_s4 = {
    'device_type' : 'cisco_ios',
    'ip' : '192.168.122.245',
    'username' : 'upawar',
    'password' : 'cisco'
}

iosv_l2_s5 = {
    'device_type' : 'cisco_ios',
    'ip' : '192.168.122.246',
    'username' : 'upawar',
    'password' : 'cisco'
}

all_devices = [iosv_l2_s1, iosv_l2_s2, iosv_l2_s3, iosv_l2_s4, iosv_l2_s5]

with open('iosv_l2_config') as f:
    lines = f.read().splitlines()
print lines

for device in all_devices:
    net_connect = ConnectHandler(**device)
    output = net_connect.send_config_set(lines)
    print output


