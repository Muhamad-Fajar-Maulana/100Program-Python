# DIBUAT OLEH MUHAMAD FAJAR MAULANA
# TANGGAL 02-11-2024
# MEMBUAT PROGRAM BOLA LAMBDA

jari_jari = int(input('Masukkan jari-jari :'))

volume = lambda r: 4/3 * 3.14 * r**3
luas = lambda r: 4 * 3.14 * r**2

print('Volume :',round(volume(jari_jari)))
print('Luas :',round(luas(jari_jari)))