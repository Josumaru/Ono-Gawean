from django.shortcuts import render
from django.http import HttpResponse
import urllib,html2text,bs4,random
# Create your views here.
def index(request):
    return render(request, "search_engine/index.html")

class ortom():
    nama = ""
    tahunBerdiri = 0000
    ketuaUmum = ""
    url = "https://muhammadiyah.or.id/?s=l"
    Pendiri=""


    def url_choose(self):
        request = urllib.request.Request(self.url)
        response = urllib.request.urlopen(request)
        resData = response.read()
        parsedhtml = bs4.BeautifulSoup(resData, "html.parser")
        urlText = parsedhtml.findAll("a",href=True)
        randomNumber = random.randint(170,190)
        getUrl = (urlText[randomNumber])
        self.url = getUrl["href"]

    def url_parse(self):
        request = urllib.request.Request(self.url)
        response = urllib.request.urlopen(request)
        resData = response.read()
        parsedhtml = bs4.BeautifulSoup(resData, "html.parser")
        urlText = parsedhtml.findAll("p")
        tupleText = str(urlText)
        txt = html2text.html2text(tupleText)
        return txt

    def time_choose(i):
        request = urllib.request.Request("https://www.islamicfinder.org/world/indonesia/1642911/jakarta-prayer-times/?language=id")
        response = urllib.request.urlopen(request)
        resData = response.read()
        parsedhtml = bs4.BeautifulSoup(resData, "html.parser")
        urlText = parsedhtml.findAll("p")
        tupleText = str(urlText[i])
        jam = html2text.html2text(tupleText)
        return jam

    def hadist_choose():
        request = urllib.request.Request("https://www.islamicfinder.org/hadith/bukhari/al-jummah-friday")
        response = urllib.request.urlopen(request)
        resData = response.read()
        parsedhtml = bs4.BeautifulSoup(resData, "html.parser")
        urlText = parsedhtml.findAll("p")
        randomNumber = random.randint(210,219)
        getText = str(urlText[randomNumber])
        text = html2text.html2text(getText)
        return text

    def hadistr_choose():
        request = urllib.request.Request("https://www.islamicfinder.org/hadith/bukhari/al-jummah-friday")
        response = urllib.request.urlopen(request)
        resData = response.read()
        parsedhtml = bs4.BeautifulSoup(resData, "html.parser")
        urlText = parsedhtml.findAll("p")
        randomNumber = random.randint(210,219)
        getText = str(urlText[randomNumber])
        text = html2text.html2text(getText)
        return text

    def date_choose():
        request = urllib.request.Request("https://www.islamicfinder.org/world/indonesia/1642911/jakarta-prayer-times/?language=id")
        response = urllib.request.urlopen(request)
        resData = response.read()
        parsedhtml = bs4.BeautifulSoup(resData, "html.parser")
        urlText = parsedhtml.findAll("p")
        getText = str(urlText[4])
        text = html2text.html2text(getText)
        return text

def userInput(request):
    if request.method == "POST":
        userIn = request.POST["search"]
        masukan = userIn.replace(" ","+")
        search = ortom()
        search.url = f"https://muhammadiyah.or.id/?s={masukan}"
        search.url_choose()
        txt = search.url_parse()
        return render (request, "search_engine/index.html",{"txt":txt})

    

def jamSholat(request):
    if request.method == "POST":
        jam = request.POST["jam"]
        getTime = ortom.time_choose(int(jam))
        getDate = ortom.date_choose()
        jamsholat = getTime+", Date : "+getDate
        return render (request, "search_engine/index.html",{"p" : jamsholat})

def getHadist(request):
    if request.method == "POST":
        request.POST["getHadist"]
        hadistGet = ortom.hadist_choose()
        return render (request, "search_engine/index.html",{"h":hadistGet})

def getNews(request):
    if request.method == "POST":
        request.POST["getHadist"]
        newsGet = ortom.hadist_choose()
        return render (request, "search_engine/index.html",{"h": newsGet})

def hw(request):
    if request.method == 'POST':
        art = "Artikel Terkait : "
        hw = ortom()
        hw.nama = "Hizbul Wathan"
        hw.tahunBerdiri = "20 Desember 1918"
        hw.ketuaUmum = "Endra Widyarsono"
        hw.Pendiri = "K.H Ahmad Dahlan"
        hw.url = "https://muhammadiyah.or.id/?s=hizbul+wathan"
        hw.url_choose()
        txt = hw.url_parse()
        return render (request, "search_engine/index.html",
        {"tahun":hw.tahunBerdiri,"pendiri": hw.Pendiri,"ketua" : hw.ketuaUmum,"nama":hw.nama,"rangkuman" : txt,"art":art})  


def Aisyiyah(request):
    if request.method == 'POST':
        art = "Artikel Terkait : "
        aisyiyah = ortom()
        aisyiyah.nama = "Aisyiyah"
        aisyiyah.tahunBerdiri = "Tahun Berdiri : 19 Mei 1917"
        aisyiyah.ketuaUmum =    "Ketua Umun : Salmah Orbayinah"
        aisyiyah.Pendiri =      "Pendiri : Siti Walidah"
        aisyiyah.url = "https://muhammadiyah.or.id/?s=aisyiyah"
        aisyiyah.url_choose()
        txt = aisyiyah.url_parse()
        return render (request, "search_engine/index.html",
        {"tahun":aisyiyah.tahunBerdiri,"pendiri":aisyiyah.Pendiri,"ketua" : aisyiyah.ketuaUmum,"rangkuman" : txt, "art":art, "nama" : aisyiyah.nama})  

def ipm(request):
    if request.method == 'POST':
        ipm = ortom()
        art = "Artikel Terkait : "
        ipm.nama = "Ikatan Pelajar Muhammadiyah"
        ipm.tahunBerdiri = " Tahun Berdir : 18 Juli 1961"
        ipm.ketuaUmum = "Ketua Umum : Ainur Rosyid Adzikkri"
        ipm.Pendiri = "Pendiri : Herman Helmi Farid Ma'ruf"
        ipm.url = "https://muhammadiyah.or.id/?s=ipm"
        ipm.url_choose()
        txt = ipm.url_parse()
        return render (request, "search_engine/index.html",
        {"tahun":ipm.tahunBerdiri,"pendiri": ipm.Pendiri,"nama":ipm.nama,"ketua" : ipm.ketuaUmum,"rangkuman" : txt,"art":art})  


def pemudaMuhammadiyah(request):
    if request.method == 'POST':
        art = "Artikel Terkait : "
        pm = ortom()
        pm.nama = "Pemuda Muhammdiyah"
        pm.tahunBerdiri = "2 Mei 1932"
        pm.ketuaUmum = "Sunanto"
        pm.Pendiri = "K.H Ahmad Dahlan"
        pm.url = "https://muhammadiyah.or.id/?s=pemuda+muhammadiyah"
        pm.url_choose()
        txt = pm.url_parse()
        return render (request, "search_engine/index.html", {"art":art,"nama": pm.nama,"tahun":pm.tahunBerdiri,"pendiri": pm.Pendiri,"ketua" : pm.ketuaUmum,"rangkuman" : txt})  
      


        