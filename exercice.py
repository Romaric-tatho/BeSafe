import socket

server_sockect = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Accesing an environment variable
value= os.environ.get('PATH')

# printing the value
print(value)
