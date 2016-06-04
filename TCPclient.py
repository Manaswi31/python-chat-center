#TCP client code in python
import socket 
import base64

TCP_IP = "127.0.0.1"
TCP_PORT = 1500

print("TCP target IP : ", TCP_IP)
print("TCP target port", TCP_PORT)
j = 0
while True:

	x = 1
	y = 2
	z = x + y
	print("z value ",z) 
	encoded = base64.b64encode(bytes(str(z), 'ascii'))
	print('encoded z', encoded)

	sock = socket.socket(socket.AF_INET, #Internet 
							socket.SOCK_STREAM) #TCP
	sock.connect((TCP_IP,TCP_PORT))

	sock.sendto(encoded, (TCP_IP, TCP_PORT))
	data = sock.recv(1024)
	print('Received data:',data)
	j = j + 1
	sock.close()

	
