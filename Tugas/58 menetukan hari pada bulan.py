# DIBUAT OLEH MUHAMAD FAJAR MAULANA
# TANGGAL 22-11-2024
# PROGRAM MENENTUKAN HARI PADA BULAN

menu_bulan = {
    "januari"   : 31,
    "februari"  : 29,
    "maret"     : 31,
    "april"     : 30,
    "mei"       : 31,
    "juni"      : 30,
    "juli"      : 31,
    "agustus"   : 31,
    "september" : 30,
    "oktober"   : 31,
    "november"  : 30,
    "desember"  : 31,
}
for bulan,hari in menu_bulan.items():
    print(f"bulan = {bulan}, jumlah hari = {hari}")
    
input_user = str(input("Masukkan nama bulan = "))

print(f"{bulan} yang anda pilih punya = {hari} hari")