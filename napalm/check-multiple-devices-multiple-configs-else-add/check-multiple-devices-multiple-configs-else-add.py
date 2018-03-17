import json
from napalm import get_network_driver

devices = ['192.168.122.242',
           '192.168.122.127']

driver = get_network_driver('ios')
iosv = driver('192.168.122.242','upawar','cisco')
iosv.open()

for device in devices:
    print "Configuring: " + str(device)
    iosv.load_merge_candidate(filename='acl.cfg')
    diffs = iosv.compare_config()
    if len(diffs) > 0:
        print(diffs)
        iosv.commit_config()
    else:
        print "No changes required"
        iosv.discard_config()
    iosv.load_merge_candidate(filename='ospf.cfg')
    diffs = iosv.compare_config()
    if len(diffs) > 0:
        print(diffs)
        iosv.commit_config()
    else:
        print "No changes required"
        iosv.discard_config()

iosv.close()

