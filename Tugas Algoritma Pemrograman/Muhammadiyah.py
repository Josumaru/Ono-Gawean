import tkinter as tk,urllib.request,urllib.parse,webbrowser, html2text,jam_sholat,re
from bs4 import BeautifulSoup
root = tk.Tk()

root.geometry("1280x720")
root.title("Muhammadiyah")


root.configure(bg = "#227C70")
label = tk.Label(root,text= "Masukan Keyword",font =("Roboto",16),bg="#227C70")
label.pack()
menu = tk.Menu(root)

canvas = tk.Canvas(root, width=100, height=20)
canvas.configure(bg="white")
canvas.pack()

stringVar = tk.StringVar()
searchBar = tk.Entry(canvas, textvariable=stringVar)
searchBar.pack(side="left")



url = f"https://muhammadiyah.or.id/?s={searchBar.get()}"
def getSearch():
    get = stringVar.get()
    requset = urllib.request.Request(url)
    response = urllib.request.urlopen(requset)
    resData = response.read()
    parsedhtml = BeautifulSoup(resData, "html.parser")
    urlText = str(parsedhtml.findAll())
    with open('link data', mode='w') as link:
        link.write(urlText)
    with open('link data', mode='r') as link:
        a = link.read()
        search_link = re.findall(r'content=[\'"]?([^\'">]+)', str(a))
        print(search_link)

    #     print(search_link)
    # search_requset = urllib.request.Request(str(search_link))
    # search_response = urllib.request.urlopen(search_requset)
    # search_resData = search_response.read()
    # search_parsedhtml = BeautifulSoup(search_resData, "html.parser")
    # search_urlText = search_parsedhtml.findAll("p")
    # search_tupleText = str(tuple(search_urlText))
    # txt = html2text.html2text(search_tupleText)
    # sc = tk.Label(root, text=txt, fg="white", font="red")
    # sc.configure(bg="#227C70")
    # sc.pack()
searchButton = tk.Button(canvas, text="Search", command=getSearch)
searchButton.pack()












# api = {
# "pemerintah"    : "https://muhammadiyah.or.id/pemerintah-anggap-isu-strategis-kesalehan-digital-muhammadiyah-konstruktif-dengan-konstitusi/",
# "nasional"      : "https://muhammadiyah.or.id/muhammadiyah-terus-bersikap-kritis-terhadap-kebijakan-nasional-namun-tidak-bersifat-oposan/",
# "pendidikan"    : "https://muhammadiyah.or.id/haedar-sampaikan-catatan-untuk-arah-pendidikan-nasional/",
# "pernikahan"    : "https://muhammadiyah.or.id/hukum-nikah-beda-agama-majelis-tarjih-haram/",
# "kuburan"       : "https://muhammadiyah.or.id/di-masjid-ada-kuburan-bolehkah-dijadikan-tempat-salat-2/",
# "arab"          : "https://muhammadiyah.or.id/pengaruh-bahasa-arab-terhadap-lahirnya-era-pencerahan-di-eropa/",
# "hutang"        : "https://muhammadiyah.or.id/tiga-prinsip-pinjam-meminjam-dalam-islam/",
# "riba"          : "https://muhammadiyah.or.id/tiga-prinsip-pinjam-meminjam-dalam-islam/",
# "dakwah"        : "https://muhammadiyah.or.id/dakwah-mesti-disampaikan-dengan-lemah-lembut-dan-teladan-yang-baik/"
#
# }


scr = tk.Scrollbar(root).pack(side="right",fill="y")

# def getSearch():
#     get = stringVar.get()
#     requset = urllib.request.Request(api[get])
#     response = urllib.request.urlopen(requset)
#     resData = response.read()
#     parsedhtml = BeautifulSoup(resData, "html.parser")
#     urlText = parsedhtml.findAll("p")
#     tupleText = str(tuple(urlText))
#     txt = html2text.html2text(tupleText)
#     sc = tk.Label(root, text=txt, fg="white", font="red")
#     sc.configure(bg="#227C70")
#     sc.pack()
# searchButton = tk.Button(canvas, text="Search", command=getSearch)
# searchButton.pack()


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
    # def userInput():
    #     v = 3
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
sholat.add_command(label="Subuh",command=jam_sholat.shubuh)
sholat.add_command(label="Dzuhur", command=jam_sholat.zhuhr)
sholat.add_command(label="Ashar",command=jam_sholat.ashr)
sholat.add_command(label="Magrib",command=jam_sholat.maghrib)
sholat.add_command(label="Isya",command=jam_sholat.isya)
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

root.mainloop()
