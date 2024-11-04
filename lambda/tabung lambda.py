# DIBUAT OLEH MUHAMAD FAJAR MAULANA
# TANGGAL 02-11-2024
# MEMBUAT PROGRAM TABUNG LAMBDA

jari_jari = int(input('Masukkan jari-jari :'))
tinggi = int(input('Masukkan tinggi :'))

volume = lambda r, t: 3.14 * r**2 * t
keliling = lambda r, t: 2 * 3.14 * r * (r + t)

print('Volume :',round(volume(jari_jari, tinggi)))
print('Keliling :',round(keliling(jari_jari, tinggi)))