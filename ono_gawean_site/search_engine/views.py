from django.shortcuts import render
from django import forms
import urllib,html2text,bs4,random
# Create your views here.
def index(request):
    return render(request, "search_engine/index.html")

def userInput(request):
    if request.method == "POST":
        search = request.POST["search"]

        baseUrl = f"https://muhammadiyah.or.id/?s={search}"
        requset = urllib.request.Request(baseUrl)
        response = urllib.request.urlopen(requset)
        resData = response.read()
        parsedhtml = bs4.BeautifulSoup(resData, "html.parser")
        urlText = parsedhtml.findAll("a",href=True)
        randomNumber = random.randint(170,190)
        getUrl = (urlText[randomNumber])
        url = getUrl["href"]

        requset = urllib.request.Request(url)
        response = urllib.request.urlopen(requset)
        resData = response.read()
        parsedhtml = bs4.BeautifulSoup(resData, "html.parser")
        urlText = parsedhtml.findAll("p")
        tupleText = str(tuple(urlText))
        txt = html2text.html2text(tupleText)
        return render (request, "search_engine/index.html",
        {"txt" : txt})

def getSearch(request):
    requset = urllib.request.Request("https://muhammadiyah.or.id/dakwah-mesti-disampaikan-dengan-lemah-lembut-dan-teladan-yang-baik/")
    response = urllib.request.urlopen(requset)
    resData = response.read()
    parsedhtml = bs4.BeautifulSoup(resData, "html.parser")
    urlText = parsedhtml.findAll("p")
    tupleText = str(tuple(urlText))
    txt = html2text.html2text(tupleText)
    return render (request, "search_engine/index.html",
    {"txt" : txt})