import json
from pyntc import ntc_device as NTC

iosv_l2 = NTC(host='192.168.122.242',username='upawar',password='cisco',device_$
iosv_l2.open()

iosv_output = iosv_l2.facts
print json.dumps(iosv_output, indent=4)

iosv_l2.close()
