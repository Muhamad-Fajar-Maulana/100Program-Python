# DIBUAT OLEH MUHAMAD FAJAR MAULANA
# TANGGAL 11-10-2024
# MEMBUAT PROGRAM TABUNG

r = int(input('Masukkan jari-jari alas tabung :'))
t = int(input('Masukkan tinggi tabung :'))
PHI = 3.14

volume = PHI * r**2 * t
keliling = 2 * PHI * r  * (r + t)

print(f'Volume :{volume}')
print(f'Keliling :{keliling}')