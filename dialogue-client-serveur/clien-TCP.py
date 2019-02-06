from socket import*
import sys 

#diapo 20

if len(sys.argv) != 2:
    print(f"Usage : {sys.argv[0]} <ip> <port>", file=sys.stderr)
    sys.exit(0)

with socket() as conn:
    conn.connect(("localhost", sys.argv[1] ))
    conn.sendall(b'GET / HTTP/1.1\r\n')
    conn.sendall(b"Host: localhost\r\n\r\n")
    text_io = conn.makefile()
    for lig in text_io:
        print(lig, end="")
    
