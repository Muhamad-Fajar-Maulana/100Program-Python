# DIBUAT OLEH MUHAMAD FAJAR MAULANA
# TANGGAL 22-11-2024
# PROGRAM DISKON BELANJA

print("Anda akan mendapatkan diskon 25% jika total belanja yang anda \nlebih dari 100 ribu")

input_user = float(input("masukkan total belanja anda = "))
diskon = input_user * 25 / 100
total_harga_diskon = input_user - diskon
if input_user >= 100:
    print(f"selamat anda mendapatkan diskon sebesar = 25%")
    print(f"diskon anda adalah = {diskon}")
    print(f"ini adalah total harga yang harus anda bayar = {total_harga_diskon}")
elif input_user < 100:
    print(f"maaf karena total belanja anda adalah = {input_user}\nmaka anda tidak mendapatkan diskon")
print("terima kasih")