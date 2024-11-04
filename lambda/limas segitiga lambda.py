# DIBUAT OLEH MUHAMAD FAJAR MAULANA
# TANGGAL 02-11-2024
# MEMBUAT PROGRAM LIMAS SEGITIGA LAMBDA

luas_alas = int(input('Masukkan luas alas :'))
luas_selubung = int(input('Masukkan luas selubung :'))
tinggi = int(input('Masukkan tinggi :'))

luas = lambda la, ls: la * ls
volume = lambda la, t: 1/3 * la * t

print('Luas :',luas(luas_alas, luas_selubung),'cm2')
print('Volume :',volume(luas_alas, tinggi),'cm3')