from flask import Flask
import socket
import threading

app = Flask(__name__)

# Flask uygulaması
@app.route('/')
def hello():
    return 'HELLO HACKATHON!'

# TCP sunucusu
def start_tcp_server():
    HOST = '127.0.0.1'
    PORT = 8000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"Sunucu {HOST}:{PORT} portunu dinliyor...")

    while True:
        client_socket, client_address = server_socket.accept()

        with client_socket:
            print(f"Istemci {client_address} bağlandı.")

            data = client_socket.recv(1024).decode('utf-8')
            print(f"İstemciden gelen mesaj: {data}")

# Sunucu ve TCP sunucusu aynı anda başlatılıyor
if __name__ == '__main__':
    # TCP sunucusunu yeni bir thread'de başlatma
    tcp_server_thread = threading.Thread(target=start_tcp_server)
    tcp_server_thread.start()

    # Flask uygulamasını çalıştırma
    app.run(debug=True, port=5000)
