import socket,sys 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect ("whois.registro.br",43)
s.send (sys.argv+"\r\n")
resposta = s.recv(1024)
print (resposta)
