# DIBUAT OLEH MUHAMAD FAJAR MAULANA
# TANGGAL 22-11-2024
# PROGRAM TUKAR NILAI UANG

print('='*30)
print('PROGRAM MENGHITUNG NALAI TUKAR PECAHAN')
print('='*30)
input = int(input('Silahkan masukkan nilai rupiah = '))
RP_5 = 1000
RP_4 = 500
RP_3 = 100
RP_2 = 50
RP_1 = 25
RP_6 = 1

input_5 = int(input / RP_5)
input = input % RP_5
input_4 = int(input / RP_4)
input = input % RP_4
input_3 = int(input / RP_3)
input = input % RP_3
input_2 = int(input / RP_2)
input = input % RP_2
input_1 = int(input / RP_1)
input = input % RP_1
input_6 = int(input / RP_6)
input = input % RP_6
print(f'Nilai rupiah yang anda masukkan setara dengan\n{input_5} kali uang 1000 rupiah\n{input_4} kali uang 500 rupiah\n{input_3} kali uang 100 rupiah\n{input_2} kali uang 50 rupiah\n{input_1} kali uang 50 rupiah\n{input_6} kali uang rupiah')