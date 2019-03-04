import pexpect

import netmiko
from netmiko import ConnectHandler

import paramiko
import os

cisco = {
'device_type': 'cisco_ios',
'host': '128.11.0.201',
'username': 'lab',
'password': 'lab',
}
net_connect = ConnectHandler(**cisco)
output = net_connect.send_command("show ip int brief")
print(output)
