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
        hw.url = "https://muhammadiyah.or.id/?s=hizbul+wathan"
        hw.url_choose()
        txt = hw.url_parse()
        return render (request, "search_engine/index.html",
        {"txt" : txt})    



        