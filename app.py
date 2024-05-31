

import tkinter as tk
from tkinter import filedialog, messagebox
import sqlite3

class QuantumKeyDistributionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quantum Anahtar Dağıtımı Simülasyonu")
        self.root.geometry("700x900") 

        # İstemci IP Adresi ve Port Girişi
        self.client_ip_label = tk.Label(root, text="İstemci IP Adresi")
        self.client_ip_label.grid(row=0, column=0, padx=10, pady=10)
        self.client_ip_entry = tk.Entry(root)
        self.client_ip_entry.grid(row=1, column=0, padx=10, pady=10)
        self.client_ip_entry.bind("<Return>", self.save_client_ip)  # Enter tuşuyla kaydetme işlevi

        # Sunucu IP Adresi ve Port Girişi
        self.server_ip_label = tk.Label(root, text="Sunucu IP Adresi")
        self.server_ip_label.grid(row=0, column=1, padx=10, pady=10)
        self.server_ip_entry = tk.Entry(root)
        self.server_ip_entry.grid(row=1, column=1, padx=10, pady=10)
        self.server_ip_entry.bind("<Return>", self.save_server_ip)  # Enter tuşuyla kaydetme işlevi

        # SQLite Veritabanına Bağlanma
        self.db_connection = sqlite3.connect('ip_adresleri.db')
        self.cursor = self.db_connection.cursor()
        self.create_table()

        # İstemci Port Girişi
        self.client_port_label = tk.Label(root, text="İstemci Port Numarası:")
        self.client_port_label.grid(row=2, column=0, padx=10, pady=10)
        self.client_port_entry = tk.Entry(root)
        self.client_port_entry.grid(row=3, column=0, padx=10, pady=10)

        # Sunucu Port Girişi
        self.server_port_label = tk.Label(root, text="Sunucu Port Numarası:")
        self.server_port_label.grid(row=2, column=1, padx=10, pady=10)
        self.server_port_entry = tk.Entry(root)
        self.server_port_entry.grid(row=3, column=1, padx=10, pady=10)

        # Quantum Anahtar Dağıtımı Butonu
        self.qkd_button = tk.Button(root, text="Anahtar Oluştur ve Paylaş", command=self.distribute_quantum_key)
        self.qkd_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # İstemci için Dosya Seçimi
        self.client_file_label = tk.Label(root, text="İstemci için Gönderilecek Veri:")
        self.client_file_label.grid(row=6, column=0, padx=10, pady=10)
        self.client_file_button = tk.Button(root, text="Dosya Seç", command=self.select_client_file)
        self.client_file_button.grid(row=6, column=1, padx=10, pady=10)
        self.client_file_path = tk.StringVar()
        self.client_file_entry = tk.Entry(root, textvariable=self.client_file_path, width=40)
        self.client_file_entry.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

        # Sunucu için Dosya Seçimi
        self.server_file_label = tk.Label(root, text="Sunucu için Gönderilecek Veri:")
        self.server_file_label.grid(row=8, column=0, padx=10, pady=10)
        self.server_file_button = tk.Button(root, text="Dosya Seç", command=self.select_server_file)
        self.server_file_button.grid(row=8, column=1, padx=10, pady=10)
        self.server_file_path = tk.StringVar()
        self.server_file_entry = tk.Entry(root, textvariable=self.server_file_path, width=40)
        self.server_file_entry.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

        # İstemci için Şifrele ve Gönder Butonu
        self.client_encrypt_button = tk.Button(root, text="Şifrele ve Gönder (İstemci)", command=self.encrypt_and_send_client_file)
        self.client_encrypt_button.grid(row=10, column=0, columnspan=2, padx=10, pady=10)

        # Sunucu için Şifrele ve Gönder Butonu
        self.server_encrypt_button = tk.Button(root, text="Şifrele ve Gönder (Sunucu)", command=self.encrypt_and_send_server_file)
        self.server_encrypt_button.grid(row=11, column=0, columnspan=2, padx=10, pady=10)
        
        # İstemci Terminali
        self.client_terminal_label = tk.Label(root, text="İstemci Terminali")
        self.client_terminal_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.client_terminal = tk.Text(root, width=60, height=6)
        self.client_terminal.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        # Sunucu Terminali
        self.server_terminal_label = tk.Label(root, text="Sunucu Terminali")
        self.server_terminal_label.grid(row=3, column=1, padx=10, pady=10, sticky="e")
        self.server_terminal = tk.Text(root, width=60, height=6)
        self.server_terminal.grid(row=4, column=1, padx=10, pady=10, sticky="e")

       
        self.delete_ip_button = tk.Button(root, text="IP Adresini Sil", command=self.delete_ip_entry)
        self.delete_ip_button.grid(row=12, column=0, columnspan=2, padx=10, pady=10)

        self.delete_all_ips_button = tk.Button(root, text="Tüm IP Adreslerini Sil", command=self.delete_all_ips)
        self.delete_all_ips_button.grid(row=13, column=0, columnspan=2, padx=10, pady=10)

        # Buton Fonksiyonlarını Ekleyin
    def delete_ip_entry(self):
            ip_address = self.client_ip_entry.get()  # Veya başka bir entry'den IP alabilirsiniz
            self.delete_ip(ip_address)

    def delete_ip(self, ip_address):
            sql = "DELETE FROM ipadresleri WHERE ip = ?"
            self.cursor.execute(sql, (ip_address,))
            self.db_connection.commit()
            print(f"{ip_address} adresi silindi.")

    def delete_all_ips(self):
            sql = "DELETE FROM ipadresleri"
            self.cursor.execute(sql)
            self.db_connection.commit()
            print("Tüm IP adresleri silindi.")

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS ipadresleri (
                               id INTEGER PRIMARY KEY,
                               ip TEXT NOT NULL)''')
        self.db_connection.commit()

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
        sql = "INSERT INTO ipadresleri (ip) VALUES (?)"
        self.cursor.execute(sql, (ip_address,))
        self.db_connection.commit()
        print("İstemci IP Adresi kaydedildi:", ip_address)

    def save_server_ip(self, event):
        ip_address = self.server_ip_entry.get()
        # Veritabanına IP adresi ekleme
        sql = "INSERT INTO ipadresleri (ip) VALUES (?)"
        self.cursor.execute(sql, (ip_address,))
        self.db_connection.commit()
        print("Sunucu IP Adresi kaydedildi:", ip_address)
     
if __name__ == "__main__":
    root = tk.Tk()
    app = QuantumKeyDistributionApp(root)
    root.mainloop()



