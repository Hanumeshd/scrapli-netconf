from scrapli_netconf.driver import NetconfDriver

my_device = {
    "host": "172.26.1.6",
    "auth_username": "root",
    "auth_password": "x1",
    "auth_strict_key": False,
    "port": 7025
}

conn = NetconfDriver(**my_device)
conn.open()
response = conn.get_config(source="running")
print(response.result)
