# DIBUAT OLEH MUHAMAD FAJAR MAULANA
# TANGGAL 25-10-2024
# MEMBUAT PROGRAM PERSEGI LAMBDA

sisi = int(input('Masukkan Sisi :'))
    
luas = lambda s: s * s
keliling = lambda s: 4 * s
    
print(f'Luas :',luas(sisi),'cm2')
print(f'Keliling :',keliling(sisi),'cm')