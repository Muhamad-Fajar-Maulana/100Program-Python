# DIBUAT OLEH MUHAMAD FAJAR MAULANA
# TANGGAL 02-11-2024
# MEMBUAT PROGRAM BALOK LAMBDA

pajang = int(input('Masukkan panjang :'))
lebar = int(input('Masukkan lebar :'))
tinggi = int(input('Masukkan tinggi :'))

luas_permukaan = lambda p, l, t: 2 * (p * l * p * t + l * t)
volume = lambda p, l, t: p * l * t

print('Luas permukaan :',luas_permukaan(pajang, lebar, tinggi))
print('Volume :',volume(pajang, lebar, tinggi))