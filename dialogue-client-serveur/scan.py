import sys, os, os.path, re
from socketserver import ThreadingTCPServer
from socket import *


for i in range(7000,7020):
    with socket() as conn:
        try: 
            conn.connect(("localhost", i))
            print("ouvert")
            
        except Exception:
            print("fermer")

sys.exit(0)