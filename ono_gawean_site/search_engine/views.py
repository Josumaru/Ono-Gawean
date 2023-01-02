from django.shortcuts import render
from django.http import HttpResponse
import urllib,html2text,bs4,random
# Create your views here.
def index(request):
    return render(request, "search_engine/index.html")

class url_usage():
    def __init__(self, url):
        self.url = url
    def url_choose(self):
        requset = urllib.request.Request(self.url)
        response = urllib.request.urlopen(requset)
        resData = response.read()
        parsedhtml = bs4.BeautifulSoup(resData, "html.parser")
        urlText = parsedhtml.findAll("a",href=True)
        randomNumber = random.randint(170,190)
        getUrl = (urlText[randomNumber])
        url = getUrl["href"]
        return url

    def url_parse(self):
        requset = urllib.request.Request(self.url)
        response = urllib.request.urlopen(requset)
        resData = response.read()
        parsedhtml = bs4.BeautifulSoup(resData, "html.parser")
        urlText = parsedhtml.findAll("p")
        tupleText = str(urlText)
        txt = html2text.html2text(tupleText)
        return txt

    def time_choose(i):
        requset = urllib.request.Request("https://www.islamicfinder.org/prayer-times/?language=id")
        response = urllib.request.urlopen(requset)
        resData = response.read()
        parsedhtml = bs4.BeautifulSoup(resData, "html.parser")
        urlText = parsedhtml.findAll("p")
        tupleText = str(urlText[i])
        jam = html2text.html2text(tupleText)
        return jam


def userInput(request):
    if request.method == "POST":
        userIn = request.POST["search"]
        search = userIn.replace(" ","+")

        baseUrl = url_usage(f"https://muhammadiyah.or.id/?s={search}")
        url = baseUrl.url_choose()

        chosen_url = url_usage(url)
        txt = chosen_url.url_parse()

        return render (request, "search_engine/index.html",
        {"txt" : txt})
i = 5
def jamSholat(request):
    if request.method == "POST":
        if request.POST["subuh"] == "subuh":
            """none"""
        jam = url_usage.time_choose(i)
        return render (request, "search_engine/index.html",{"p" : jam})
       