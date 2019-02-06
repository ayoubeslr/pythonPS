import sys, os, os.path, re
from socketserver import ThreadingTCPServer
from socket import *


sock_server = socket()
sock_server .bind(("", int(sys.argv[1])))
sock_server.listen(4)
print("Le serveur ecoute sur le port " + sys.argv[1], file=sys.stderr)
print("Son repertoir de base est ",file=sys.stderr)

while True:
    try:
        sock_client, adr_client = sock_server.accept()
        print("connexion de ".format(adr_client[0]))
        threrading.Thread(target=traiter_client, args=(sock_client,)).start
    except KeyboardInterrupt:
        break

sock_server.shutdown(SHUT_RDWR)
print("arret du server")
for t in reading.enumerate():
    if t != threading.main_thread(): t.join
sys.exit(0)