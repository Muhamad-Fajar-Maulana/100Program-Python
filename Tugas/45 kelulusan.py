# DIBUAT OLEH MUHAMAD FAJAR MAULANA
# TANGGAL 22-11-2024
# PROGRAM KELULUSAN SISWA

print('='*30)
print('PROGRAM KELULUSAN'.center(30))
print('='*30)

input_nilai = float(input('Silahkan masukkan nilai anda: '))
if input_nilai >= 94:
    print('Anda lulus dengan prefikat A')
elif 80 < input_nilai < 90:
    print('Anda lulus dengan predikat B')
elif 70 < input_nilai < 80:
    print('Anda lulus dengan predikat C')
else:
    print('Maaf anda dinyatakan tidak lulus/silahkan coba lagi tahun depan :)')