# DIBUAT OLEH MUHAMAD FAJAR MAULANA
# TANGGAL 22-11-2024
# PROGRAM MENETUKAN BILANGAN

x = int(input('Masukkan bilangan bulat 1 = '))
y = int(input('Masukkan bilangan bulat 2 = '))
z = int(input('Masukkan bilangan bulat 3 = '))

if x > y and x > z:
    print(f'Ini adalah bilangan terbesar {x}')
elif y > x and y > z:
    print(f'Ini adalah bilangan terbesar {y}')
elif z > x and z > y:
    print(f'Ini adalah bilangan terbesar {z}')
else:
    print()
if x < y and x < z:
    print(f'Ini adalah bilangan terkecil {x}')
elif y < x and y < z:
    print(f'Ini adalah bilangan terkecil {x}')
elif z < x and z < y:
    print(f'Ini adalah bilangan terkecil {x}')