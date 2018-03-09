import json
from napalm import get_network_driver

bgplist = ['192.168.122.242',
           '192.168.122.127']

for device in bgplist:
    print "Getting info of: " + str(device)
    driver = get_network_driver('ios')
    iosv_device = driver(device,'upawar','cisco')
    iosv_device.open()
    bgp_neighbors = iosv_device.get_bgp_neighbors()
    print json.dumps( bgp_neighbors, indent=4) + '\n'
    iosv_device.close()

