# DIBUAT OLEH MUHAMAD FAJAR MAULANA
# TANGGAL 22-11-2024
# PROGRAM MENETUKAN HURUF

import os
os.system('cls')
huruf = str(input('Masukkan abjad dari A-Z = '))
vokal = ['a','i','u','e','o']
kosonan = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
bukan_huruf = [vokal,kosonan]
if huruf in vokal:
    print(f'{huruf} merupakan huruf vokal')
elif huruf in kosonan:
    print(f'{huruf} merukan huruf konsonan')
elif huruf not in bukan_huruf:
    print(f'{huruf} bukan huruf')