
import tkinter as tk
from tkinter import filedialog, messagebox
import mysql.connector

class QuantumKeyDistributionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quantum Key Distribution Simulation")
        self.root.geometry("700x900") 

        # IP Address and Port Entry for Client
        self.client_ip_label = tk.Label(root, text="İstemci IP ADRESİ")
        self.client_ip_label.grid(row=0, column=0, padx=10, pady=10)
        self.client_ip_entry = tk.Entry(root)
        self.client_ip_entry.grid(row=1, column=0, padx=10, pady=10)
        self.client_ip_entry.bind("<Return>", self.save_client_ip)  # Enter tuşuyla kaydetme işlevi

        # IP Address and Port Entry for Server
        self.server_ip_label = tk.Label(root, text="Sunucu IP ADRESİ")
        self.server_ip_label.grid(row=0, column=1, padx=10, pady=10)
        self.server_ip_entry = tk.Entry(root)
        self.server_ip_entry.grid(row=1, column=1, padx=10, pady=10)
        self.server_ip_entry.bind("<Return>", self.save_server_ip)  # Enter tuşuyla kaydetme işlevi

        # Connect to MySQL Database
        self.db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # XAMPP varsayılan şifresi boş olabilir veya ayarladığınız şifreyi girin
            database="ipadresleri"
        )

        # Veritabanı bağlantısı başarılıysa
        if self.db_connection.is_connected():
            print("MySQL veritabanına başarıyla bağlanıldı")
            self.cursor = self.db_connection.cursor()
        else:
            print("MySQL veritabanına bağlanırken bir hata oluştu")
        
        # Port Entry for Client
        self.client_port_label = tk.Label(root, text="İstemci Port Numarası:")
        self.client_port_label.grid(row=2, column=0, padx=10, pady=10)
        self.client_port_entry = tk.Entry(root)
        self.client_port_entry.grid(row=3, column=0, padx=10, pady=10)

        # Port Entry for Server
        self.server_port_label = tk.Label(root, text="Sunucu Port Numarası:")
        self.server_port_label.grid(row=2, column=1, padx=10, pady=10)
        self.server_port_entry = tk.Entry(root)
        self.server_port_entry.grid(row=3, column=1, padx=10, pady=10)

        # Quantum Key Distribution Button
        self.qkd_button = tk.Button(root, text="Anahtar Oluştur ve Paylaş", command=self.distribute_quantum_key)
        self.qkd_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # File Selection for Encryption for Client
        self.client_file_label = tk.Label(root, text="İstemci için Gönderilecek Veri:")
        self.client_file_label.grid(row=6, column=0, padx=10, pady=10)
        self.client_file_button = tk.Button(root, text="Dosya Seç", command=self.select_client_file)
        self.client_file_button.grid(row=6, column=1, padx=10, pady=10)
        self.client_file_path = tk.StringVar()
        self.client_file_entry = tk.Entry(root, textvariable=self.client_file_path, width=40)
        self.client_file_entry.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

        # File Selection for Encryption for Server
        self.server_file_label = tk.Label(root, text="Sunucu için Gönderilecek Veri:")
        self.server_file_label.grid(row=8, column=0, padx=10, pady=10)
        self.server_file_button = tk.Button(root, text="Dosya Seç", command=self.select_server_file)
        self.server_file_button.grid(row=8, column=1, padx=10, pady=10)
        self.server_file_path = tk.StringVar()
        self.server_file_entry = tk.Entry(root, textvariable=self.server_file_path, width=40)
        self.server_file_entry.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

        # Encrypt and Send Button for Client
        self.client_encrypt_button = tk.Button(root, text="Şifrele ve Gönder (İstemci)", command=self.encrypt_and_send_client_file)
        self.client_encrypt_button.grid(row=10, column=0, columnspan=2, padx=10, pady=10)

        # Encrypt and Send Button for Server
        self.server_encrypt_button = tk.Button(root, text="Şifrele ve Gönder (Sunucu)", command=self.encrypt_and_send_server_file)
        self.server_encrypt_button.grid(row=11, column=0, columnspan=2, padx=10, pady=10)
        
        # Terminal for Client
        self.client_terminal_label = tk.Label(root, text="İstemci Terminali")
        self.client_terminal_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.client_terminal = tk.Text(root, width=60, height=6)
        self.client_terminal.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        # Terminal for Server
        self.server_terminal_label = tk.Label(root, text="Sunucu Terminali")
        self.server_terminal_label.grid(row=3, column=1, padx=10, pady=10, sticky="e")
        self.server_terminal = tk.Text(root, width=60, height=6)
        self.server_terminal.grid(row=4, column=1, padx=10, pady=10, sticky="e")

    def distribute_quantum_key(self):
        # Anahtar dağıtımı işlemleri burada gerçekleştirilir.
        pass

    def select_client_file(self):
        self.client_file_path.set(filedialog.askopenfilename())

    def select_server_file(self):
        self.server_file_path.set(filedialog.askopenfilename())

    def encrypt_and_send_client_file(self):
        # İstemci için dosya şifreleme ve gönderme işlemleri burada gerçekleştirilir.
        pass

    def encrypt_and_send_server_file(self):
        # Sunucu için dosya şifreleme ve gönderme işlemleri burada gerçekleştirilir.
        pass

    def save_client_ip(self, event):
        ip_address = self.client_ip_entry.get()
        # Veritabanına IP adresi ekleme
        sql = "INSERT INTO ipadresleri (ip) VALUES (%s)"
        val = (ip_address,)
        self.cursor.execute(sql, val)
        self.db_connection.commit()
        print("İstemci İp Adresi kaydedildi:", ip_address)

    def save_server_ip(self, event):
        ip_address = self.server_ip_entry.get()
        # Veritabanına IP adresi ekleme
        sql = "INSERT INTO ipadresleri (ip) VALUES (%s)"
        val = (ip_address,)
        self.cursor.execute(sql, val)
        self.db_connection.commit()
        print("Sunucu İp Adresi kaydedildi:", ip_address)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuantumKeyDistributionApp(root)
    root.mainloop()


