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

output = net_connect.send_command("sh ver | i up")
print(output)

<<<<<<< HEAD
output = net_connect.send_command("sh inventory raw")
=======

output = net_connect.send_command("sh proto")
>>>>>>> c651c274db43cef15d765658b3a06dd996153d1e
print(output)

