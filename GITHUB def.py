
print("---MENU---")
print("Ayam Bakar")
print("Ayam Goreng")
n = input('Masukkan pilihan anda : ').lower()
print(n)
def ayam(ayam, bakar, goreng):
    if n == "ayam bakar":
        print(ayam + bakar)
    elif n == "ayam goreng":
        print(ayam + goreng)
    else:
        print("saya kurang mengerti dengan yang anda ketikkan")
ayam(8000, 6000, 4000)
while True:
    a = input('mau apa lagi jika ia ketik iya jika tidak ketik tidak : ').lower()
    if a == 'ya':
        d = 1
        while d <= 3:
            z = input("ayam bakar atau ayam goreng : ")
            if z == "ayam bakar":
                ayam(8000, 6000, 4000)
            elif z == "ayam goreng":
                ayam(8000, 6000, 4000)
            else:
                print("saya kurang mengerti dengan yang anda ketikkan")
                print('jika ingin mengensel ketik secara asal sebanyak 3 kali')
            d += 1
                

    elif a == "tidak":
        print("terima kasih")
        break

    else:
        print("saya kurang mengerti dengan yang anda ketikkan")
