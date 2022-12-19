def hitung_kecepatan():
  print('Komputer akan membantu anda menghitung kecepatan')
  jarak = float(input('masukkan jarak: '))
  waktu = float(input('masukkan jarak: '))
  kecepatan = jarak * waktu
  print('Kecepatan = ', kecepatan, '\n')

def luas_segitiga():
  print('Komputer akan membantu anda menghitung luas segitiga')
  alas = float(input('masukkan alas: '))
  tinggi = float(input('masukkan tinggi: '))
  luasSegitiga = 1/2 * alas * tinggi
  print('Luas segitiga = ', luasSegitiga, '\n')

def luas_balok():
  print('Komputer akan membantu anda menghitung luas balok')
  panjang = float(input('masukkan panjang: '))
  lebar = float(input('masukkan lebar: '))
  tinggi = float(input('masukkan tinggi: '))
  luas = 2*panjang*lebar + 2*panjang*tinggi + 2*lebar*tinggi
  print('Luas balok = ', luas, '\n')

def luas_bola():
  print('Komputer akan membantu anda menghitung luas bola')
  r = float(input('Masukkan jari-jari: '))
  luas = 4 * 3.14 * (r**2)
  print('Luas bola = ', luas, '\n')


while True:
  userInput = int(input(
    'Pilih rumus yang akan digunakan: \n\n1. Kecepatan\n2. Luas segitiga\n3. Luas balok\n4. Luas bola\n0. Keluar\n\nPilih nomor berapa gan??: '))
  if (userInput == 1):
    hitung_kecepatan()
  elif (userInput == 2):
    luas_segitiga()
  elif (userInput == 3):
    luas_balok()
  elif(userInput == 4):
    luas_bola()
  else:
    break