import time 

def penghitungWaktu(t):
    while t :
        menit, detik = divmod(t, 60)
        waktu = '{:02d}:{:02d}'.format(menit, detik)
        print(waktu, end ='\r')
        time.sleep(1)
        t -= 1

    print("Waktu habis")

t = input("masukkan waktu : ")

penghitungWaktu5 (int(t))