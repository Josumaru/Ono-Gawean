class lingkaran():
    def __init__(self, r):
        self.perbandingan = r
    def __eq__(self, objek):
        return self.perbandingan == objek.perbandingan
    def __ne__(self, objek):
        return self.perbandingan != objek.perbandingan
    def __it__(self, objek):
        return self.perbandingan <  objek.perbandingan
    def __le__(self, objek):
        return self.perbandingan <= objek.perbandingan
    def __gt__(self, objek):
        return self.perbandingan >  objek.perbandingan
    def __ge__(self, objek):
        return self.perbandingan >= objek.perbandingan

print("----masukkan 3 jari jari----")
print("masukkan jari jari lingkaran")

p = input("masukkan yang ingin dibandingkan : ")
z = input("masukkan yang ingin dibandingkan : ")
l = input("masukkan yang ingin dibandingkan : ")

P = lingkaran(p)
Z = lingkaran(z)
L = lingkaran(l)

print("--------nilai perbandingan--------")
print("             P = ", p)
print("             Z = ", z)
print("             L = ", l)
print("permadingan yang bisa kamu gunakan")
print("  ( == ) ", "( != )", "( < )", "( <= )", "( > )", "( >= )")
print("jika ingin menyudahi ketik keluar")

m = input("massukan perbandingn : ").upper()

while True:    
    if m == "P == L":
        print(P == L)
        m = input("massukan perbandingn : ").upper()
    elif m == "P == Z":
        print(P == Z)
        m = input("massukan perbandingn : ").upper()
    elif m == "Z == P":
        print(Z == P)
        m = input("massukan perbandingn : ").upper()
    elif m == "Z == L":
        print(Z == L)
        m = input("massukan perbandingn : ").upper()
    elif m == "L == P":
        print(L == P)
        m = input("massukan perbandingn : ").upper()
    elif m == "Z == P":
        print(Z == P)
        m = input("massukan perbandingn : ").upper()
    elif m == "P < L":
        print(P < L)
        m = input("massukan perbandingn : ").upper()
    elif m == "P < Z":
        print(P < Z)
        m = input("massukan perbandingn : ").upper()
    elif m == "Z < P":
        print(Z < P)
        m = input("massukan perbandingn : ").upper()
    elif m == "Z < L":
        print(Z < L)
        m = input("massukan perbandingn : ").upper()
    elif m == "L < P":
        print(L < P)
        m = input("massukan perbandingn : ").upper()
    elif m == "Z < P":
        print(Z < P)
        m = input("massukan perbandingn : ").upper()
    elif m == "P <= L":
        print(P <= L)
        m = input("massukan perbandingn : ").upper()
    elif m == "P <= Z":
        print(P <= Z)
        m = input("massukan perbandingn : ").upper()
    elif m == "Z <= P":
        print(Z <= P)
        m = input("massukan perbandingn : ").upper()
    elif m == "Z <= L":
        print(Z <= L)
        m = input("massukan perbandingn : ").upper()
    elif m == "L <= P":
        print(L <= P)
        m = input("massukan perbandingn : ").upper()
    elif m == "Z <= P":
        print(Z <= P)
        m = input("massukan perbandingn : ").upper()
    elif m == "P > L":
        print(P > L)
        m = input("massukan perbandingn : ").upper()
    elif m == "P > Z":
        print(P > Z)
        m = input("massukan perbandingn : ").upper()
    elif m == "Z > P":
        print(Z > P)
        m = input("massukan perbandingn : ").upper()
    elif m == "Z > L":
        print(Z > L)
        m = input("massukan perbandingn : ").upper()
    elif m == "L > P":
        print(L > P)
        m = input("massukan perbandingn : ").upper()
    elif m == "Z > P":
        print(Z > P)
        m = input("massukan perbandingn : ").upper()
    elif m == "P >= L":
        print(P >= L)
        m = input("massukan perbandingn : ").upper()
    elif m == "P >= Z":
        print(P >= Z)
        m = input("massukan perbandingn : ").upper()
    elif m == "Z >= P":
        print(Z >= P)
        m = input("massukan perbandingn : ").upper()
    elif m == "Z >= L":
        print(Z >= L)
        m = input("massukan perbandingn : ").upper()
    elif m == "L >= P":
        print(L >= P)
        m = input("massukan perbandingn : ").upper()
    elif m == "Z >= P":
        print(Z >= P)
        m = input("massukan perbandingn : ").upper()
    elif m == "P != L":
        print(P != L)
        m = input("massukan perbandingn : ").upper()
    elif m == "P != Z":
        print(P != Z)
        m = input("massukan perbandingn : ").upper()
    elif m == "Z != P":
        print(Z != P)
        m = input("massukan perbandingn : ").upper()
    elif m == "Z != L":
        print(Z != L)
        m = input("massukan perbandingn : ").upper()
    elif m == "L != P":
        print(L != P)
        m = input("massukan perbandingn : ").upper()
    elif m == "Z != P":
        print(Z != P)
        m = input("massukan perbandingn : ").upper()
    elif m == "keluar":
        exit()
