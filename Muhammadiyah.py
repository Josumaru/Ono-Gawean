import urllib.request
with urllib.request.urlopen("https://muhammadiyah.or.id/sejarah-muhammadiyah/") as response:
    file = response.read()
    print(file)