import re
import os.path
from collections import Counter

print('Aplikasi Hitung Frekuensi Karakter Teks Dokumen')
print('I Gusti Ayu Mirah Agung Jayanti (1808561057)\nMata Kuliah Kriptoanalisis\n')

file = input('Masukkan Nama Dokumen: ')
# Cek dokumen yang dicari tanpa ekstensi .txt
if(file.find('.txt') == -1):
    file = file+'.txt'
if (os.path.exists(file)):
    a = bool(1)
else:
    print('File Yang Anda Masukkan Tidak Ditemukan!')
    exit()

if (os.path.exists(file)):
    # Buka dokumen
    file = open(file, 'r+')
# Baca baris pertama dokumen
string = ((' ').join(line.strip() for line in file))

# Konversi ke lower string
mystring = string.lower()

# Cek Alphabet
cek = re.compile('[^a-zA-Z]')
mystring = cek.sub('', mystring)

# Menganalisa n (banyak karakter) dengan dokumen
jml = int(input('Masukkan Jumlah Karakter Yang Akan Dianalisis: '))
frekuensi = {}
array = [(mystring[i:i + jml]) for i in range(0, len(mystring), jml)]
frekuensi = Counter(array)

# Mencetak output
print('\nHasil Analisis:')
hitung=0
for i in sorted(frekuensi):
    hitung += 1
    print('Karakter: ' + i + ',\t| Karakter Yang Sama: ' + str(frekuensi[i]) + ',\t| Peluang : ' + str(1/int(frekuensi[i])))
print('Total Karakter Keseluruhan: ' + str(hitung))