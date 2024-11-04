# DIBUAT OLEH MUHAMAD FAJAR MAULANA
# TANGGAL 25-10-2024
# MEMBUAT PROGRAM JAJAR GENJANG LAMBDA

alas = int(input('Masukkan Alas :'))
tinggi = int(input('Masukkan Tinggi :'))
sisi_miring = int(input('Masukkan Sisi miring :'))

luas = lambda a, t: a * t
keliling = lambda a, sm: 2 * a + sm

print('Luas :',luas(alas, tinggi))
print('Keliling :',keliling(alas, sisi_miring))