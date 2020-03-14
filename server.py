import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('server socket created')
s.bind((socket.gethostname(),1024))
print('server socket binded')
s.listen(5)
print('server socket is  listining')
clt,add=s.accept()
print(f "Connection to(adr)established")
clt.send(bytes("Socket programming in python","utf-8"))

while True:
   num = clt.recv(1024)
   print(num)
   num=num.decode('utf-8')
   if int(num)%2==0:
      clt.send(bytes(f' {num},is a even number','utf-8'))
   else
      clt.send(bytes(f' {num},is a odd number','utf-8'))
