import socket
import sys

#################################################################
############    Simple Portscan in py by crypto   ###############
############ => https://github.com/CryptoSecurityx ##############
#################################################################
#################################################################
try:
	host = sys.argv[1]  # pega o host alvo
	portlist = [8080,21,80,443,445,3306,25,22,82,8081] # cria uma lista de portas
	for porta in portlist: # testa porta por porta da portlist
		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		client.settimeout(0.1)
		resposta = client.connect_ex((host, porta))

		if resposta == 0:
			print(f"{porta}  Aberta")
		else:
			print(f"{porta} Fechada")

except socket.error:
	print(f"Conexao Recusada")


except IndexError:
	print('#################################################################')
	print('############    Simple Portscan by crypto   ###############')
	print('############ => https://github.com/CryptoSecurityx ##############')
	print('#################################################################')
	print("Usage: portscan.py <host>")
