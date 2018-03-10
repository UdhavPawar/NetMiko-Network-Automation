import json
from napalm import get_network_driver

driver = get_network_driver('ios')
iosv = driver('192.168.122.242','upawar','cisco')
iosv.open()

print "Configuring ACL on 192.168.122.242"
iosv.load_merge_candidate(filename='acl.cfg')
iosv.commit_config()
iosv.close()

