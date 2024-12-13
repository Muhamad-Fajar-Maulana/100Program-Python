# DIBUAT OLEH MUHAMAD FAJAR MAULANA
# TANGGAL 22-11-2024
# PROGRAM KALKULATOR SEDEHANA

input_user = str(input('Silahkan operator (+, -, %, /, x, **)'))
angka_1 = float(input('Masukkan angka 1 = '))
angka_2 = float(input('Masukkan angka 2 = '))

if input_user == "+":
    hasil = angka_1 + angka_2
    print(f"hasilnya adalah {hasil}")
elif input_user == "-":
    hasil = angka_1 - angka_2
    print(f"hasilnya adalah {hasil}")
elif input_user == "%":
    hasil = angka_1 % angka_2
    print(f"hasilnya adalah {hasil}")
elif input_user == "/":
    hasil = angka_1 / angka_2
    print(f"hasilnya adalah {hasil}")
elif input_user == "*":
    hasil = angka_1 * angka_2
    print(f"hasilnya adalah {hasil}")
elif input_user == "**":
    hasil = angka_1 ** angka_2
    print(f"hasilnya adalah {hasil}")
print("terima kasih")