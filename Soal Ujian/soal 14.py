# DIBUAT OLEH MUHAMAD FAJAR MAULANA
# TANGGAL 19-11-2024
# MENGERJAKAN SOAL UJIAN NO 14

huruf = input('Masukkan huruf (A-ZA): ').upper()

if huruf in 'AIUEO':
    print(huruf, 'Adalah huruf vokal')
elif huruf in 'BCDFGHJKLMNPQRSTVWXYZ':
    print(huruf, 'Adalah huruf konsonan')
else:
    print(huruf, 'Bukan huruf alfabet')