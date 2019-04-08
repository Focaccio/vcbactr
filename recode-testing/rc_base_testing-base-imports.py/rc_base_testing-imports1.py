#rc=recode i.e. not gafc / not greg (good) af (areaf) code
# test editing from git hub bowser
#from __future__ import print_function
import argparse
import subprocess
import configparser
import glob
import os
import paramiko
import pexpect
import re
import select
import shutil
import signal
import string
import sys
import syslog
import time
import traceback
import io
# necessary for fnxs
import netlib



from binascii import *
from cmd import *
from ftplib import *
from netmiko import *
from optparse import *
from paramiko import *
from paramiko.ssh_exception import *
from paramiko.py3compat import *
# from pyRouterLib import *
from io import StringIO
from io import BytesIO