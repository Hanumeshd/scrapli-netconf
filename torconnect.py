from ncclient import manager
from pprint import pprint
import xmltodict
from tor_info import tor_1
from tor_info import tor_2
with manager.connect(host=tor_1["host"], port=tor_1["port"], username=tor_1["username"], password=tor_1["password"], hostkey_verify=False) as m:
	for capability in m.server_capabilities:
  		print(capability)

with manager.connect(host=tor_2["host"], port=tor_2["port"], username=tor_2["username"], password=tor_2["password"], hostkey_verify=False) as m:
	for capability in m.server_capabilities:
 		 print(capability)
