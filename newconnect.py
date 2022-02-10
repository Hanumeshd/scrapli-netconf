from scrapli_netconf.driver import NetconfDriver

my_device = {
    "host": "172.26.1.40",
    "auth_username": "wsvm",
    "auth_password": "wsvm",
    "auth_strict_key": False,
    "port": 830
}

conn = NetconfDriver(**my_device)
conn.open()
response = conn.get_config(source="running")
print(response.result)
