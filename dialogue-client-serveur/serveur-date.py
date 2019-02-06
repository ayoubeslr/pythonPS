from socket import *
import sys
import datetime
import logging 
from logging.handlers import RotatingFileHandlerfrom

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s %(message)s')
file_handler = RotatingFileHandler('serveurUdp.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <port>", file=sys.stderr)
    sys.exit(1)

TAILLE_TAMPON = 256
sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', int(sys.argv[1])))
print("Serveur en attente sur le port " + sys.argv[1], file=sys.stderr)


while True:
    try:
        date = datetime.datetime.now()
        requete = sock.recvfrom(TAILLE_TAMPON)
        (mess, adr_client) = requete
        ip_client, port_client = adr_client
        message = mess.decode().upper()
        print(f"Requête provenant de {ip_client}. Longueur = {len(mess)}",file=sys.stderr)
        if message=="DATE":
            reponse = str(date.day)+"/"+str(date.month)+"/"+str(date.year)
            logger.info("creating...")
            a = auxiliary_module.Auxiliary()
            
        sock.sendto(reponse.encode(), adr_client)
    except KeyboardInterrupt: breack

sock.close()
print("Arrêt du serveur", file=sys.stderr)
sys.exit(0)