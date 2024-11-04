# DIBUAT OLEH MUHAMAD FAJAR MAULANA
# TANGGAL 25-10-2024
# MEMBUAT PROGRAM TRAPESIUM LAMBDA

sisi_atas = int(input('Masukkan Sisi atas :'))
sisi_bawah = int(input('Masukkan Sisi bawah :'))
tinggi = int(input('Masukkan Tinggi :'))
a = int(input('Masukkan Sisi A :'))
b = int(input('Masukkan Sisi B :'))
c = int(input('Masukkan Sisi C :'))
d = int(input('Masukkan Sisi D :'))

luas = lambda sa, sb, t: 1/2 * (sa + sb) * t
keliling = lambda A, B, C, D: A + B + C + D

print('Luas :',luas(sisi_atas, sisi_bawah, tinggi))
print('Keliling :',keliling(a, b, c, d))