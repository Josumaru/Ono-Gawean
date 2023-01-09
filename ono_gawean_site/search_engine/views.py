from django.shortcuts import render
from django.http import HttpResponse
import urllib,html2text,bs4,random
# Create your views here.
def index(request):
    return render(request, "search_engine/index.html")

class ortom():
    tahunBerdiri = 0000
    ketuaUmum = ""
    url = "url website"
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
        search = userIn.replace(" ","+")

        baseUrl = ortom()
        baseUrl.url = f"https://muhammadiyah.or.id/?s={search}"
        url = baseUrl.url_choose()

        chosen_url = ortom()
        chosen_url.url = url
        txt = chosen_url.url_parse()

        return render (request, "search_engine/index.html",
        {"txt" : txt})

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
        hw = ortom()
        hw.tahunBerdiri = "20 Desember 1918"
        hw.ketuaUmum = "Endra Widyarsono"
        hw.Pendiri = "K.H Ahmad Dahlan"
        hw.url = "https://muhammadiyah.or.id/?s=hizbul+wathan"
        hw.url_choose()
        txt = hw.url_parse()
        return render (request, "search_engine/index.html",
        {"txt" : txt})    

def Aisyiyah(request):
    if request.method == 'POST':
        aisyiyah = ortom()
        aisyiyah.tahunBerdiri = "19 Mei 1917"
        aisyiyah.ketuaUmum = "Salmah Orbayinah"
        aisyiyah.Pendiri = "K.H Ahmad Dahlan"
        aisyiyah.url = "https://muhammadiyah.or.id/?s=aisyiyah"
        aisyiyah.url_choose()
        txt = aisyiyah.url_parse()
        return render (request, "search_engine/index.html",
        {"txt" : txt})  

def ipm(request):
    if request.method == 'POST':
        ipm = ortom()
        ipm.tahunBerdiri = "18 Juli 1961"
        ipm.ketuaUmum = "Ainur Rosyid Adzikkri"
        ipm.Pendiri = "Herman Helmi Farid Ma'ruf"
        ipm.url = "https://muhammadiyah.or.id/?s=ipm"
        ipm.url_choose()
        txt = ipm.url_parse()
        return render (request, "search_engine/index.html",
        {"txt" : txt})    

def pemudaMuhammadiyah(request):
    if request.method == 'POST':
        pm = ortom()
        pm.tahunBerdiri = "2 Mei 1932"
        pm.ketuaUmum = "Sunanto"
        pm.Pendiri = "K.H Ahmad Dahlan"
        pm.url = "https://muhammadiyah.or.id/?s=pemuda+muhammadiyah"
        pm.url_choose()
        txt = pm.url_parse()
        return render (request, "search_engine/index.html",
        {"txt" : txt})       


        