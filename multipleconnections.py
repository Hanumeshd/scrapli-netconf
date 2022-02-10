
from scrapli_netconf.driver import NetconfDriver
devices = [{
    "host": "172.26.1.100",
    "auth_username": "root",
    "auth_password": "x1",
    "auth_strict_key": False,
    "port": 830,
}, {
    "host": "172.26.1.40",
    "auth_username": "wsvm",
    "auth_password": "wsvm",
    "auth_strict_key": False,
    "port": 830,
}]
for device in devices:
  conn = NetconfDriver(**devices[device])
  conn.open()
  response = conn.get_config(source="running")
  print(response.result)

