#nama class
class mobil:
#fungsi init disertai parameter
  def __init__(self, merek, kecepatan, jumlahMaksimalPenumpang):
#variabel 
    self.merek = merek
    self.kecepatan = kecepatan
    self.jumlahMaksimalPenumpang = jumlahMaksimalPenumpang
#method
  def Merek(self):
    return self.merek

  def Kecepatan(self):
    return self.kecepatan

  def Penumpang(self):
    return self.jumlahMaksimalPenumpang
#pemanggilan class
m = mobil("Civic Type R","235 km/jam", "4")
#menampilkan hasil
print("Merek Mobil:", m.Merek())
print("Kecepatan Mobil: ", m.Kecepatan())
print("Penumpang Maksimal:", m.Penumpang())
