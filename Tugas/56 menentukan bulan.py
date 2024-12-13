# DIBUAT OLEH MUHAMAD FAJAR MAULANA
# TANGGAL 22-11-2024
# PROGRAM MENENTUKAN BULAN

menu_bulan = {
    "januari"   : 1,
    "februari"  : 2,
    "maret"     : 3,
    "april"     : 4,
    "mei"       : 5,
    "juni"      : 6,
    "juli"      : 7,
    "agustus"   : 8,
    "september" : 9,
    "oktober"   : 10,
    "november"  : 11,
    "desember"  : 12,
}
for bulan,angka in menu_bulan.items():
    print(f'Bulan = {bulan}, angka = {angka}')
    
input_user = int(input('Masukkan angka sesuai bulan = '))

print(f'Angka yang anda pilih adalah bulan = {bulan}')

# if input_user == 1:
#     print(f"")