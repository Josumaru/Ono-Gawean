data = {'Pulsa':'anda adalah 5000','Kartu':'Masa aktif kartu anda sampai 31 Desember 2022','Kuota':'anda sebesar 3 Gb','Nelpon':'Saat ini belum ada promo nelpon','Sms':'Saat ini belum ada promo sms','UpgradeSIM':'Permintaan anda sedang kami proses'}
def tampilkanPulsa():
    pulsa = data['Pulsa']
    print ('Pulsa', pulsa)
def tampilkanKartu():
    kartu = data['Kartu']
    print ('Kartu', kartu)
def tampilkanKuota():
    kuota = data['Kuota']
    print ('Kuota', kuota)
def tampilkanNelpon():
    nelpon = data['Nelpon']
    print ('Nelpon', nelpon)
def tampilkanSms():
    sms = data['Sms']
    print ('Sms', sms)
def tampilkanUpgradeSIM():
    upgradesim = data['UpgradeSIM']
    print ('UpgradeSIM', upgradesim)

print('Selamat datang di layanan informasi pengguna')
print('Pilihan yang tersedia :')
print('0 menampilkan bantuan ini')
print('1 menampilkan Info Pulsa')
print('2 menampilkan Info Kartu')
print('3 menampilkan Info Kuota')
print('4 menampilkan Info Nelpon')
print('5 menampilkan Info SMS')
print('6 menampilkan Upgrade SIM')
print('00 menampilkan Keluar')
while True:
    inp = input('Masukkan Pilihan :')
    if inp == '0':
        print('Pilihan yang tersedia :')
        print('0 menampilkan bantuan ini')
        print('1 menampilkan Info Pulsa')
        print('2 menampilkan Info Kartu')
        print('3 menampilkan Info Kuota')
        print('4 menampilkan Info Nelpon')
        print('5 menampilkan Info SMS')
        print('6 menampilkan Upgrade SIM')
        print('00 menampilkan Keluar')
    elif inp == '1':
        print,tampilkanPulsa()
    elif inp == '2':
        print,tampilkanKartu()
    elif inp == '3':
        print,tampilkanKuota()
    elif inp == '4':
        print,tampilkanNelpon()
    elif inp == '5':
        print,tampilkanSms()
    elif inp == '6':
        print,tampilkanUpgradeSIM()
        break
    elif inp == '00':
        print('Terima Kasih')
        break
    else:
        print('Pilihan Tidak Dikenal')