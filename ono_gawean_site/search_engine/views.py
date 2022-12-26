from django.shortcuts import render
from django import forms
import webbrowser, urllib,html2text,bs4
# Create your views here.
def index(request):
    return render(request, "search_engine/index.html")



api = {
"pemerintah"    : "https://muhammadiyah.or.id/pemerintah-anggap-isu-strategis-kesalehan-digital-muhammadiyah-konstruktif-dengan-konstitusi/",
"nasional"      : "https://muhammadiyah.or.id/muhammadiyah-terus-bersikap-kritis-terhadap-kebijakan-nasional-namun-tidak-bersifat-oposan/",
"pendidikan"    : "https://muhammadiyah.or.id/haedar-sampaikan-catatan-untuk-arah-pendidikan-nasional/",
"pernikahan"    : "https://muhammadiyah.or.id/hukum-nikah-beda-agama-majelis-tarjih-haram/",
"kuburan"       : "https://muhammadiyah.or.id/di-masjid-ada-kuburan-bolehkah-dijadikan-tempat-salat-2/",
"arab"          : "https://muhammadiyah.or.id/pengaruh-bahasa-arab-terhadap-lahirnya-era-pencerahan-di-eropa/",
"hutang"        : "https://muhammadiyah.or.id/tiga-prinsip-pinjam-meminjam-dalam-islam/",
"riba"          : "https://muhammadiyah.or.id/tiga-prinsip-pinjam-meminjam-dalam-islam/",
"dakwah"        : "https://muhammadiyah.or.id/dakwah-mesti-disampaikan-dengan-lemah-lembut-dan-teladan-yang-baik/"

}
#get = input("Y :")

class forms(forms.Form):
    submit = forms.CharField(max_length=20)
    
def go(request):
    if request.method == "POST":
        isian = forms(request.POST)
        if isian.is_valid():
            submit = isian.form.cleaned_data["submit"]
            return render(request, "search_engine/index.html")
        #submit = request.POST["submit"]
        return render (request, "search_engine/index.html", {"submit" : submit})
    else :
        return render (request, "search_engine/index.html")

def getSearch(request):
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    requset = urllib.request.Request("https://muhammadiyah.or.id/dakwah-mesti-disampaikan-dengan-lemah-lembut-dan-teladan-yang-baik/")
    response = urllib.request.urlopen(requset)
    resData = response.read()
    parsedhtml = bs4.BeautifulSoup(resData, "html.parser")
    urlText = parsedhtml.findAll("p")
    tupleText = str(tuple(urlText))
    txt = html2text.html2text(tupleText)
    return render (request, "search_engine/index.html",
    {"txt" : txt})




# def show_text(request):
#     webbrowser.open_new_tab("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
#     text = "ini string"
#     return render (request,"index.html",
#     {"text : text"})