from server.chat_server import ChatServer

#The line means that we allow you to connect with any host (any IP and Hostname).
#You can explicitly write a localhost or 127.0.0.1, then it will only work on one computer.
chat_server = ChatServer(5000, '[::]')
chat_server.serve()

