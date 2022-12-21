import tkinter as tk
import pandas
from tkinter import ttk
from time import strftime
from datetime import time

my_font = ('times', 52, 'bold')  # display size and style

# mengolah data jadwal sholat
data = pandas.read_csv('Jadwal Sholat Yogyakarta, Daerah Istimewa Yogyakarta, Indonesia - Tahun 2021 M.csv').to_dict()
df = pandas.DataFrame(data)
tanggal = strftime("%d/%m")


def shubuh(data=df, tanggal=tanggal):
    shubuh_dict = {
        row.Tanggal:row.Shubuh for (index, row) in df.iterrows()
    }
    waktu_sholat = shubuh_dict[f"{tanggal}/2021"]
    sholat = 'shubuh'
    jamsekarang(waktu_sholat, sholat)


def zhuhr(data=df, tanggal=tanggal):
    zhuhr_dict = {
        row.Tanggal:row.Zhuhr for (index, row) in df.iterrows()
    }
    waktu_sholat = zhuhr_dict[f"{tanggal}/2021"]
    sholat = 'zhuhr'
    jamsekarang(waktu_sholat, sholat)

def ashr(data=df, tanggal=tanggal):
    ashr_dict = {
        row.Tanggal:row.Ashar for (index, row) in df.iterrows()
    }
    waktu_sholat = ashr_dict[f"{tanggal}/2021"]
    sholat = 'ashr'
    jamsekarang(waktu_sholat, sholat)

def maghrib(data=df, tanggal=tanggal):
    maghrib_dict = {
        row.Tanggal:row.Maghrib for (index, row) in df.iterrows()
    }
    waktu_sholat = maghrib_dict[f"{tanggal}/2021"]
    sholat = 'maghrib'
    jamsekarang(waktu_sholat, sholat)

def isya(data=df, tanggal=tanggal):
    isya_dict = {
        row.Tanggal:row.Isya for (index, row) in df.iterrows()
    }
    waktu_sholat = isya_dict[f"{tanggal}/2021"]
    sholat = 'isya'
    jamsekarang(waktu_sholat, sholat)

def jamsekarang(waktu_sholat, sholat):
    my_w = tk.Tk()
    my_w.geometry("545x300")
    def my_time():
        time_string = strftime('%H:%M:%S %p')  # time format
        l1.config(text=time_string)
        l1.after(1000, my_time)  # time delay of 1000 milliseconds
    def selisih_waktu(waktu_sholat=waktu_sholat ):
        jam = int(strftime('%H'))
        menit = int(strftime('%M'))
        jam_sholat = int(waktu_sholat[:2])
        menit_sholat=int(waktu_sholat[4:6])

        hours = jam_sholat - jam
        if hours < 0:
            hours = hours + 24
        min = menit_sholat - menit
        if min < 0:
            min = min + 60
        mine.config(text= f"masih ada {hours} jam dan {min} menit lagi sebelum sholat {sholat} kembali")


    my_font = ('times', 52, 'bold')  # display size and style
    l1 = tk.Label(my_w, font=my_font, bg='green')
    l1.grid(row=1, column=1, padx=5, pady=25)
    mine = tk.Label(my_w, font=('times', 15, 'bold'))
    mine.grid(row=3, column=1, pady=10)
    waktu = tk.Label(my_w ,font=('times', 15, 'bold'), text=f"waktu sholat {sholat} tanggal {tanggal} jam {waktu_sholat}")
    waktu.grid(row=2, column=1)
    my_time()
    selisih_waktu()
    my_w.mainloop()



