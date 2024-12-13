# DIBUAT OLEH MUHAMAD FAJAR MAULANA
# TANGGAL 22-11-2024
# PROGRAM DISKON BELANJA BIASA

print('='*30)
print('PROGRAM MENENTUKAN DISKON BELANJA'.center(30))
print('='*30)

total_harga = float(input('Masukkan total harga: '))
if total_harga >= 100:
    total_harga * 5 / 100
    print('Selamat anda medapatkan diskon sebesar 5%')
elif total_harga < 100:
    print('Maaf anda tidak mendapatkan diskon')
diskon = total_harga * 5 / 100
print(f'Ini adalah diskon anda = {diskon}')
total_diskon_harga = total_harga - diskon
print(f'Ini adalah harga yang harus anda bayar = {total_diskon_harga}')