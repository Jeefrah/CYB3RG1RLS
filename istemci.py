import socket

# Sunucunun IP adresi ve port numarası
HOST = '127.0.0.1'
PORT = 8000

# TCP soketi oluşturma ve sunucuya bağlanma
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))

    # Sunucuya gönderilecek mesaj
    message = "Merhaba, bu bir test mesajıdır."

    # Mesajı sunucuya gönder
    client_socket.sendall(message.encode('utf-8'))

    print(f"Sunucuya gönderilen mesaj: {message}")
