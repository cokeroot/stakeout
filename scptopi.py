from http import client
import paramiko
from scp import SCPClient
# function to estaablish parameters
def createsshclient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client
# filling in ssh parameters
server = "raspberrypi.local"
port = 22
user = "pi"
password = "password"
# initializing the ssh connection with said parameters
ssh = createsshclient(server, port, user, password)
scp = SCPClient(ssh.get_transport())
# select file to send to established host
scp.put('C:\\Users\\unfai\\OneDrive\\Desktop\\capstone\\shalome.txt')
