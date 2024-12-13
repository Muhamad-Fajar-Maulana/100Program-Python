# DIBUAT OLEH MUHAMAD FAJAR MAULANA
# TANGGAL 22-11-2024
# PROGRAM MENGHITUNG WAKTU PROYEK

print('='*30)
print('PROGRAM MENGHITUNG WAKTU PROYEK')
print('='*30)

hari_input = float(input('Masukkan waktu pengerjaan proyek: '))
TAHUN = 365
BULAN = 12
HARI = 1
# yang memakai huruf besar semua iti konstanta
# artinya nilai yang berada di konstanta tersebut
# tidak akan diubah

tahun = int(hari_input / TAHUN)
hari_input = hari_input % TAHUN
bulan = int(hari_input / BULAN)
hari_input = hari_input % BULAN
hari = int(hari_input / HARI)
hari_input = hari_input % HARI

print(f'Waktu pengerjaan proyek ini adalah\n tahun = {tahun}\nbulan = {bulan}\nhari = {hari}')