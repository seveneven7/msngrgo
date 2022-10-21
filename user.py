import time, socket, sys
socket_server = socket.socket()
server_host = socket.gethostname()
ip = socket.gethostbyname(server_host)
sport = 8080
print('{Это ваш IP адрес}', ip)
server_host = input('{Укажите IP адрес вашего друга} ')
name = input('{Напишите имя вашего друга} ')
socket_server.connect((server_host, sport))
socket_server.send(name.encode())
server_name = socket_server.recv(1024)
server_name = server_name.decode()
print(server_name, '{Присоединился} ')
while True:
  message = (socket_server.recv(1024)).decode()
  print(server_name, ":", message)
  message = input("{Вы} ")
  socket_server.send(message.encode())
