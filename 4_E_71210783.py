# Deret Geometri

u = int(input("Suku ke : "))
un = int(input("Suku yang dituju : "))
a = float(input("Angka awal : "))
r = float(input("rasio selisih : "))

hasil = 0

for n in range(u, un+1):
    suku = a * (r**(n-1))
    print(suku)

print('Jumlah suku', suku)
