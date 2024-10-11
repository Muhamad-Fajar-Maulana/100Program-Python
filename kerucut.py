# DIBUAT OLEH MUHAMAD FAJAR MAULANA
# TANGGAL 11-10-2024
# MEMBUAT PROGRAM KERUCUT

r = int(input('Maukkan jari-jari alas kerucut :'))
t = int(input('Masukkan tinggi kerucut :'))

s = (r**2 + t**2)
volume = (1/3) * r**2 * t
luas_permukaan = r * (r + t)
luas_selimut =  r * s

print(f'Volume :{round(volume)}')
print(f'Luas permukaan :{round(luas_permukaan)}')
print(f'Luas selimut :{round(luas_selimut)}')