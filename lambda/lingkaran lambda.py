# DIBUAT OLEH MUHAMAD FAJAR MAULANA
# TANGGAL 25-10-2024
# MEMBUAT PROGRAM LINGKARAN LAMBDA

jari_jari = int(input('Masukkan jari-jari :'))

diameter = lambda r: r * 2
keliling = lambda r: 2 * 3.14 * r

print('Diameter :',diameter(jari_jari))
print('Keliling :',keliling(jari_jari))