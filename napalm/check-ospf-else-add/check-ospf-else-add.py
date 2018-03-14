import json
from napalm import get_network_driver

configs = ['acl.cfg','ospf.cfg']

driver = get_network_driver('ios')
iosv = driver('192.168.122.242','upawar','cisco')
iosv.open()

for config in configs:
    print "Configuring " + str(config) + " on 192.168.122.242"
    iosv.load_merge_candidate(filename=str(config))
    diffs = iosv.compare_config()
    if len(diffs) > 0:
        print(diffs)
        iosv.commit_config()
    else:
        print "No changes required"
        iosv.discard_config()

iosv.close()

