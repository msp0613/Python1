import socket
s = socket.socket()
port = 56789
print("PROBA NAWIAZANIA POLACZENIA...")
try:
    s.connect_ex(('127.0.0.1', port))
    print("POLACZENIE NAWIAZANE")
    print(s.recv(1024))
except socket.error as err:
        print(err)
else: 
    user_input = 0
    print("DANE:")
    print("FRAZA END KONCZY EDYCJE")
    while(user_input != "END"):
        user_input = input()
        if(user_input != "END"):
             s.send(user_input.encode())
        else:
            s.send('ZAKONCZYL EDYCJE'.encode())
            print("ZAMYKANIE POLACZENIA...")
            s.close()



