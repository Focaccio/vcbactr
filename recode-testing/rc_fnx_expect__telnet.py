# rc=recode
# fnx == function
# epxpect= moule
# function nam
# def login_to_node ():
# use Telnet
   try:
        child = pexpect.spawn('telnet %s' % (host))
        child.expect('Username:')
        child.sendline(switch_username)
        child.expect('Password:')
        child.sendline(switch_telnet_password)
        child.expect('#')
       print(("Successfully Telnetted to host "), (host))
   except:
       try:
           #child.expect('>')
           child.sendline('enable')
            child.expect('Password:')
            child.sendline(switch_enable_password)
            child.expect('#')
           print(("Successfully Telneted to host "), (host), (',and enabled console'))
       except:
           print(("Failed to Telnet to host "), (host))
   return