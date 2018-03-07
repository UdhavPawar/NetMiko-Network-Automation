import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosv_sw = driver('192.168.122.242','upawar','cisco')
iosv_sw.open()

ios_output = iosv_sw.get_facts()
print json.dumps( ios_output, indent=4)

ios_output = iosv_sw.get_interfaces()
print json.dumps( ios_output, indent=4)

ios_output = iosv_sw.get_interfaces_counters()
print json.dumps( ios_output, indent=4)

