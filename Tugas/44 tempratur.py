# DIBUAT OLEH MUHAMAD FAJAR MAULANA
# TANGGAL 22-11-2024
# PROGRAM KONVERSI TEMPRATUR

print('='*30)
print('PROGRAM KONVERSI TEMPRATUR'.center(30))
print('='*30)

celcius = float(input('Masukkan suhu dalam celcius: '))
print('suhu dalam reamur = ',celcius, 'celcius')

reamur = (4/5) * celcius
print('Suhu dalam reamur = ',reamur, 'reamur')

farenhait = ((9/5) * celcius) + 32
print('Suhu dalam farenhait = ',farenhait, 'farenhait')

kelvin = celcius + 273
print('Suhu dalam kelvin = ',kelvin, 'kelvin')