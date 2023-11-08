''' String Python '''
# Format String
umur = 28
nama = 'Rusdiana'
text = 'Hi, perkenalkan nama saya \"{1}\", berumur {0} tahun'
print(text.format(umur, nama))

# Mengiris String
print(nama[3:]) # dari index 3 sampai akhir
print(nama[:5]) # dari awal sampai index 5 (exclude 5)

''' Method String '''
# Semua method string mengembalikan nilai baru
a = 'rusdiana'
b = 'Rusdiana'

c = 'saya suka apel, karena apel mengandung vitamin'
print(a.capitalize()) # Huruf kapital diawal string
print(b.casefold()) # Return lower casefol
print(b.center(len(b), 'o')) # return center char
if c:
  panjang_c = len(c)
print(c.count('apel', 0, panjang_c)) # Berapa kali sebuah string muncul
print(c.encode())