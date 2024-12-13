# DIBUAT OLEH MUHAMAD FAJAR MAULANA
# TANGGAL 22-11-2024
# PROGRAM NILAI SISWA

print('='*30)
print('PROGRAM MENETUKAN NILAI UJIAN'.center(30))
print('='*30)
nilai = float(input('Masukkan nilai anda = '))
if nilai >= 90 and nilai <= 100 :
    # kalo pengen 2 situasi dalam 1 if yaitu pake
    # and
    print('Nalai anda = A')
elif nilai >= 80 and nilai <= 90:
    print('Nialai anda = B')
elif nilai >= 70 and nilai <= 80:
    print('Nilai anda = C')
elif nilai <= 60:
    print('Nilai anda = E')
    
print('Belajarlah lebih giat lagi')