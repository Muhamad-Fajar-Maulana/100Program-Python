# DIBUAT OLEH MUHAMAD FAJAR MAULANA
# TANGGAL 02-11-2024
# MEMBUAT PROGRAM KERUCUT LAMBDA

jari_jari = int(input('Masukkan jari-jari :'))
tinggi = int(input('Masukkan tinggi :'))
x = int(input('Masukkan sisi :'))

sisi = lambda r, t: (r**2 + t**2)
volume = lambda r, t: (1/3) * r**2 * t
luas_permukaan = lambda r, t: r * (r + t)
luas_sisi = lambda r, s: r * s

print('Sisi :',sisi(jari_jari, tinggi))
print('Volume :',volume(jari_jari, tinggi))
print('Luas permukaan :',luas_permukaan(jari_jari, tinggi))
print('Luas sisi :',luas_sisi(jari_jari, x))