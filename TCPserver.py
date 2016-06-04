#TCP server code in python
import socket 
import base64

TCP_IP = "127.0.0.1"
TCP_PORT = 1500


print("TCP target IP : ", TCP_IP)
print("TCP target port", TCP_PORT)
j = 0
while True:
	sock = socket.socket(socket.AF_INET, #Internet 
						socket.SOCK_STREAM) #TCP

	sock.bind((TCP_IP, TCP_PORT))
	sock.listen(1)
	z,addr = sock.accept()
	print('Connection address:', addr)

	while True:
		data = z.recv(20) #buffer size is 1024 bytes
		if not data: break
		decode = base64.b64decode(data)
		print("Received message:", data, decode)
		z.send(data) #echo
	j = j + 1
	z.close()
