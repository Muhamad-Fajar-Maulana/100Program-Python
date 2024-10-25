# DIBUAT OLEH MUHAMAD FAJAR MAULANA
# TANGGAL 11-10-2024
# MEMBUAT PROGRAM BALOK

panjang = int(input('Masukkan panjang :'))
lebar = int(input('Masukkan lebar :'))
tinggi = int(input('Masukkan tinggi :'))

luas_permukaan = 2 * (panjang * lebar * panjang  + lebar * tinggi)
volume = panjang * lebar * tinggi

print(f'Luas permukaan :{luas_permukaan}')
print(f'Volume :{volume}')