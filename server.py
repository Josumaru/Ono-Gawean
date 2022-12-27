import socket
from math import pi

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50002))
s.listen(5)
print("Server siap")

msg = ""
r = 0
t = 0

while msg != "keluar":
    komm, addr = s.accept()
    while msg != "keluar":
        item = komm.recv(1024).decode().lower().split("=")
        msg = item[0]
        if msg == "keluar":
            komm.send("done".encode())
            s.close()
            break
        print("Pesan : ", msg())
        if len(item) == 2:
            if msg == "jarijari":
                r = int(item[1])
                komm.send("jarijari disimpan".encode())
            elif msg == "tinggi":
                t = int(item[1])
                komm.send("tinggi disimpan".encode())
            else:
                komm.send("perintah tidak diketahui".encode())
        elif msg == "hitung":
            L = float((pi*r**2) + (2*pi*r*t))
            response = f"Luas tabung dengan jari-jari {r} dan tinggi {t} adalah {L}"
            komm.send(response.encode())
        else:
            komm.send("pesan tidak diketahui".encode())
