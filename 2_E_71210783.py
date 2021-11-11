nama = input("Nama : ")
tl = input("Tempat Tanggal Lahir : ")

x = nama.split(" ",1)
y = tl.split(" ",1)

print("Haloo!",x[1],",",x[0])
print("Anda lahir di",y[0],y[1])
