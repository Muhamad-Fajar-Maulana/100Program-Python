# DIBUAT OLEH MUHAMAD FAJAR MAULANA
# TANGGAL 22-11-2024
# PROGRAM KONPERSI PANJANG BENDA

input_m = float(input('Masukkan panjang benda dengan satuan m = '))

INCHI = 25.4
KAKI = 30.48
YARD = 0.9144

inchi = input_m / INCHI
input_m = input_m % INCHI
kaki = input_m / KAKI
input_m = input_m % KAKI
yard = input_m / YARD
input_m = input_m % YARD

print(f'Ini adalah konversi panjang benda\ninchi = {inchi:.2f}\nkaki = {kaki:.2f}\nyard = {yard:.2f}')