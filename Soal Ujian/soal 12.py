# DIBUAT OLEH MUHAMAD FAJAR MAULANA
# TANGGAL 19-11-2024
# MENGERJAKAN SOAL UJIAN NO 12

nilai_siswa = int(input('Masukkan nilai siswa (0-100): '))

if 90 <= nilai_siswa <= 100:
    nilai = 'A'
elif 80 <= nilai_siswa < 90:
    nilai = 'B'
elif 70 <= nilai_siswa < 80:
    nilai = 'C'
elif 60 <= nilai_siswa < 70:
    nilai = 'D'
else:
    nilai = 'E'
    
print("Nilai: ",nilai)