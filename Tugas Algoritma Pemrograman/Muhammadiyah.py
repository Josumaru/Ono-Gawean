import tkinter as tk,urllib.request,urllib.parse,webbrowser,re
import jam_sholat
root = tk.Tk()
root.geometry("1280x720")
root.title("Muhammadiyah")
root.configure(bg = "#227C70")
label = tk.Label(root,text= "Semua pencarian anda ada disini",font =("Roboto",16),bg="#227C70")
label.pack()
menu = tk.Menu(root)

canvas = tk.Canvas(root, width=720, height=34)
canvas.configure(bg="green")
canvas.pack()

searchBar = tk.Entry(root)
canvas.create_window(360,17, window=searchBar)

url = "https://muhammadiyah.or.id/tiga-prinsip-pinjam-meminjam-dalam-islam/"

requset = urllib.request.Request(url)
response = urllib.request.urlopen(requset)
resData = response.read()


class content():
    def text():
        urlText = re.findall(r"<p>(.*?)</p>",str(resData))
        for x in urlText:
            r = x
            sc = tk.Label(root, text=r)
            sc.pack()
    # def showContent():
    #     sc = tk.Label(root, text="apa ya")

    
class barMenu():
    def close():
        """Exit command"""
        exit()
    def about():
        """Contains about the Ono-Gawean group"""
        overlay= tk.Tk()
        overlay.title("About")
        label = tk.Label(overlay,text="Created by Ono-Gawean\n\nMember:\n1.\n2.\n3.\n4.\n5.\n6.\n7.\n8.\n9.\n10.")
        label.pack()
    def userInput():
        v = 3
class link():
    def web():
        webbrowser.open_new_tab("https://muhammadiyah.or.id/")
    def ig():
        webbrowser.open_new_tab("https://www.instagram.com/lensamu/?hl=id")
    def yt():
        webbrowser.open_new_tab("https://www.youtube.com/channel/UCVvgJXxcJ20rhR8tcjY77jQ")
    def tw():
        webbrowser.open_new_tab("https://twitter.com/muhammadiyah")
    def fb():
        webbrowser.open_new_tab("https://www.facebook.com/PersyarikatanMuhammadiyah/")
    

# home menubar
home = tk.Menu(menu, tearoff=0)
home.add_command(label="SignIn")
home.add_command(label="Login")
home.add_command(label="Exit",command=barMenu.close)
menu.add_cascade(label="Home",menu=home)

# settings menubar

helpmenu = tk.Menu(menu, tearoff=0)
helpmenu.add_command(label="Tips & Trick")
helpmenu.add_command(label="Documentation")
helpmenu.add_command(label="About", command=barMenu.about)
menu.add_cascade(label="help", menu=helpmenu)

# news
news = tk.Menu(menu, tearoff=0)
news.add_command(label="Muktamar")
news.add_command(label="UMS")
news.add_command(label="Ketum Muhammadiyah")
menu.add_cascade(label="News", menu=news)


# Jadwal Sholat
sholat = tk.Menu(menu, tearoff=0)
sholat.add_command(label="Subuh", command=jam_sholat.shubuh)
sholat.add_command(label="Dzuhur")
sholat.add_command(label="Ashar")
sholat.add_command(label="Ashar")
sholat.add_command(label="Magrib")
sholat.add_command(label="Isya")
menu.add_cascade(label="Jadwal Sholat", menu=sholat)
root.config(menu=menu)

# Social Media
sm = tk.Menu(menu, tearoff=0)
sm.add_command(label="Website",command=link.web)
sm.add_command(label="Instagram",command=link.ig)
sm.add_command(label="Youtube",command=link.yt)
sm.add_command(label="Twitter",command=link.tw)
sm.add_command(label="Facebook",command=link.fb)
menu.add_cascade(label="Social Media", menu=sm)

root.config(menu=menu)

searchButton = tk.Button(root, text="Search", command=content.text)
searchButton.pack()

root.mainloop()
