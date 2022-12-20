import tkinter as tk
import pandas
from tkinter import ttk

my_w = tk.Tk()
my_w.geometry("405x300")
from time import strftime


def my_time():
    time_string = strftime('%H:%M:%S %p')  # time format
    l1.config(text=time_string)
    l1.after(1000, my_time)  # time delay of 1000 milliseconds


my_font = ('times', 52, 'bold')  # display size and style

# mengolah data jadwal sholat
data = pandas.read_csv('Jadwal Sholat Yogyakarta, Daerah Istimewa Yogyakarta, Indonesia - Tahun 2021 M.csv').to_dict()
df = pandas.DataFrame(data)

def shubuh(data=df):
    shubuh_dict = {
        row.Tanggal:row.Shubuh for (index, row) in df.iterrows()
    }

def zhuhr(data=df):
    zhuhr_dict = {
        row.Tanggal:row.Zhuhr for (index, row) in df.iterrows()
    }

def ashr(data=df):
    ashr_dict = {
        row.Tanggal:row.Ashr for (index, row) in df.iterrows()
    }

def maghrib(data=df):
    maghrib_dict = {
        row.Tanggal:row.Shubuh for (index, row) in df.iterrows()
    }

def isya(data=df):
    isya_dict = {
        row.Tanggal:row.Isya for (index, row) in df.iterrows()
    }


l1 = tk.Label(my_w, font=my_font, bg='green')
l1.grid(row=1, column=1, padx=5, pady=25)

shubuh()

my_time()
my_w.mainloop()
