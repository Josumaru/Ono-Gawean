import socket

msg = ""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 50002))
print("Menghitung luas tabung")

while msg.lower() != "keluar":
    msg = input("Pesan: ")
    s.send(msg.encode())
    if msg.lower() == "keluar":
        response = s.recv(1024).decode()
        print("Response: -")
        s.close()
        break
    elif msg.lower() != "keluar":
        response = s.recv(1024).decode()
        print("Respon: ", response)
s.close()
