# DIBUAT OLEH MUHAMAD FAJAR MAULANA
# TANGGAL 25-10-2024
# MEMBUAT PROGRAM SEGITIGA LAMBDA

alas = int(input('Masukkan Alas :'))
tinggi = int(input('Masukkan Tinggi :'))

luas = lambda a, t: 1/2 * a * t

print('Luas :',luas(alas, tinggi))