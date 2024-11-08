# IBUAT OLEH MUHAMAD FAJAR MAULANA
# TANGGAL 08-11-2024
# MENGERJAKAN SOAL UJIAN NO 8

print('===========================')
print('======PROGRAM TABUNG=======')

tinggi = float(input('Masukkan tinggi tabung: '))
jari_jari = float(input('Masukkan jari-jari tabung: '))

volume_tabung = 2 * 3.14 * jari_jari * tinggi
luas_permukaan_tabung = 3.14 * jari_jari * jari_jari * 2 * 3.14 * jari_jari

print('Volume tabung: ',round(volume_tabung))
print('Luas permukaan tabung: ',round(luas_permukaan_tabung))