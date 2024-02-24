import socket
import os

try:
    print("URUCHAMIANIE SERWERA....")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 56789
    s.bind(('', port))
except socket.error as err:
    print(err) 
    s.close()
else:
    print("SERWER URUCHOMIONY PRAWIDLOWO NA PORCIE ", port)
    s.listen(5)
    print("NASLUCHIWANIE ROZPOCZETE")
    while(True):
        c, addr = s.accept()
        print("POLACZENIE NAWIAZANE Z ADRESU ", addr)
        message = ("SERWER:POLACZENIE NAWIAZANE")
        c.send(message.encode())
        mess = s.connect_ex(('127.0.0.1', port))
        print(str(mess))
