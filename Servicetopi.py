from pickle import FALSE, TRUE
import time
import random
from pathlib import Path
from windowsservice import SMWinservice
from http import client
import paramiko
from scp import SCPClient

def createsshclient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client

class pythoncornerexample(SMWinservice):
    _svc_name_ = "pLEASEWORK"
    _svc_display_name_ = "Please work"
    _svc_description_ = "Thats a cool service"


    def start(self):
        self.isrunning = TRUE

    def stop(self):
        self.isrunning = FALSE

    def main(self):
       server = "raspberrypi.local"
       port = 22
       user = "pi"
       password = "password"
       ssh = createsshclient(server, port, user, password)
       scp = SCPClient(ssh.get_transport())
       scp.put('C:\\Users\\unfai\\OneDrive\\Desktop\\capstone\\shalome.txt')       
if __name__ == '__main__':
    pythoncornerexample.parse_cmd()
