from socket import *
import sys

if len(sys.argv) != 3:
    print(f"Usage : {sys.argv[0]} <ip> <port>", file=sys.stderr)
    sys.exit(0)

TAILLE_TAMPON = 256

with socket(AF_INET, SOCK_DGRAM) as sock:
    mess = input("Entrez une commande (help pour la liste, quit pour quitter) :")
    sock.sendto(mess.encode(), (sys.argv[1], int(sys.argv[2])))
    
    reponse, _= sock.recvfrom(TAILLE_TAMPON)
    print("Reponse = "+ reponse.decode())