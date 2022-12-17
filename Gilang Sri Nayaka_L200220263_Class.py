class tiket:
    def __init__(self,nama,tribun,sektor,harga):
        self.nama = nama
        self.tribun = tribun
        self.sektor = sektor
        self.harga = harga
    def nama(self):
        return self.nama

    def tribun(self):
        return self.tribun

    def sektor(self):
        return self.sektor

    def harga(self):
        return self.harga

d = tiket("GilangSN","Selatan",3,"Rp75.000")

print("Berikut Pesanan Anda:")
print('Nama     :',d.nama)
print('Tribun   :',d.tribun)
print('Sektor   :',d.sektor)
print('Harga    :',d.harga)
