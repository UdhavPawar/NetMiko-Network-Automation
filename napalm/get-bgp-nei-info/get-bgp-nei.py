import json
from napalm import get_network_driver
driver = get_network_driver('ios')

iosv_sw = driver('192.168.122.242','upawar','cisco')
iosv_sw.open()
bgp_neighbors = iosv_sw.get_bgp_neighbors()
print 'SWITCH:'
print json.dumps( bgp_neighbors, indent=4)
iosv_sw.close()

iosv_rtr = driver('192.168.122.127','upawar','cisco')
iosv_rtr.open()
bgp_neighbors = iosv_rtr.get_bgp_neighbors()
print 'ROUTER:'
print json.dumps( bgp_neighbors, indent=4)
iosv_rtr.close()

