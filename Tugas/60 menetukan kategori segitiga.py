# DIBUAT OLEH MUHAMAD FAJAR MAULANA
# TANGGAL 22-11-2024
# PROGRAM MENENTUKAN KATEGORI SEGITIGA

print("dengan syarat berikut\n1 . a+b>c\n2.a+c>b\n3.b+c>a\njika tidak sesuai maka bukan segitiga ! ! !")
print()
a = float(input("masukkan sisi a = "))
b = float(input("masukkan sisi b = "))
c = float(input("masukkan sisi terpanjang c = "))

# c merupakan sisi terpanjang

if a**2 + b**2 == c**2:
    print("ini adalah segitiga siku siku")
elif a**2 + b**2 > c**2:
    print("ini adalah segitiga lancip")
if a**2 + b**2 < c**2:
    print("ini adalah segitiga tumpul")