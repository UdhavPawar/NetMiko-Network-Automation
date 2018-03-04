from netmiko import ConnectHandler

iosv_l2_s1 = {
    'device_type':'cisco_ios',
    'ip':'192.168.122.242',
    'username':'upawar',
    'password':'cisco',
}

iosv_l2_s2 = {
    'device_type':'cisco_ios',
    'ip':'192.168.122.243',
    'username':'upawar',
    'password':'cisco',
}

iosv_l2_s3 = {
    'device_type':'cisco_ios',
    'ip':'192.168.122.244',
    'username':'upawar',
    'password':'cisco',
}

iosv_l2_s4 = {
    'device_type':'cisco_ios',
    'ip':'192.168.122.245',
    'username':'upawar',
    'password':'cisco',
}

iosv_l2_s5 = {
    'device_type':'cisco_ios',
    'ip':'192.168.122.246',
    'username':'upawar',
    'password':'cisco',
}

devices = [iosv_l2_s1, iosv_l2_s2, iosv_l2_s3, iosv_l2_s4, iosv_l2_s5]

for device in devices:
    print "Configuring Loopback for: ",device['ip'],'\n'
    d = str((devices.index(device)) + 1)
    net_connect =  ConnectHandler(**device)
    output = net_connect.send_command('sh ip int br')
    print output,'\n'
    config_command = ['no int loop 0']
    output = net_connect.send_config_set(config_command)
    print output,'\n'
    output = net_connect.send_command('sh ip int br')
    print output,'\n'


