# DIBUAT OLEH MUHAMAD FAJAR MAULANA
# TANGGAL 11-10-2024
# MEMBUAT PROGRAM LIMAS SIGITIGA

la = int(input('Masukkan luas alas :'))
ls = int(input('Masukkan uas selubung :'))
t = int(input('Masukkan tinggi :'))

luas = la * ls
volume = 1/3 * la * t

print(f'Luas :{round(luas)}','cm2')
print(f'Volume :{round(volume)}','cm3')