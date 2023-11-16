# Method String

# Konversi karakter pertama menjadi kapital
a = "hello, world!"
A = a.capitalize()
print(A)

# Konversi karakter ke huruf kecil
B = "HELLO WORLD"
b = B.casefold()
print(b)

# Meratakan string ditengah = string.center(length, character)
c = "Pisang"
center = c.center(20, '-')
print(center) # ------Pisang-------

# Menghitung kemunculan sebuah nilai dalam string = string.count(value, start, end)
d = "Saya cinta pisang, karena pisang kesukaan saya"
count_d = d.count("pisang", 1, 50)
print(count_d)

# Mengkodekan string = string.encode(encoding=encoding, errors=errors)
e = "i love you"
e_encoding = e.encode(encoding="ascii", errors="replace")
print(e_encoding)

# Memeriksa string diakhiri dengan ... = string.endswith(value, start, end)
f = "Hello, world!"
cek = f.endswith("!")
print(cek)

# Mengatur ukuran tab pada string = string.expandtabs(tabsize)
g = "H\te\tl\tl\to"
tab_g = g.expandtabs(10)
print(tab_g) # H                e               l               l           o

# Pencarian string = string.find(value, start, end)
# => mengembalikan no index kemunculan pertama
h = "Mustang merk mobil dari ford"
word = h.find("o")
print(word) # 14

# Formating string = string.format(value1, value2...)
# gunakan indexing atau key=value, atau placeholde kosong {}
text = "Masukan {nama} dalam ingatan {any}"
result_text = text.format(nama = "Rusdiana", any = "Masyarakat")
print(result_text)
# catatan tambahan
'''
:< = Rata kiri hasilnya (dalam ruang yang tersedia)
:> = Meratakan hasilnya ke kanan (dalam ruang yang tersedia)
:^ = Tengah menyelaraskan hasilnya (dalam ruang yang tersedia)
:= = Tempatkan tanda pada posisi paling kiri
:+ = Gunakan tanda tambah untuk menunjukkan apakah hasilnya positif atau negatif
:- = Gunakan tanda minus hanya untuk nilai negatif
:  = Gunakan spasi untuk menyisipkan spasi tambahan sebelum bilangan positif (dan tanda minus sebelum bilangan negatif)
:, = Gunakan koma sebagai pemisah ribuan
:_ = Gunakan garis bawah sebagai pemisah ribuan
:b = Format binner
:f = Memformat nomer dengan titik, gunakan angka seletah "." dan sebelum "f"
'''

# Mencari teks dalam string = string.index(value, start, end)
# sama dengan find(), tapi jika text tidak ditemukan. index akan menghasilkan error

# Memeriksa apakah string dalam alfanumerik, return bool = string.isalnum()
i = "Company12"
result_i = i.isalnum()
print(result_i) # True

# Returns True if all characters in the string are in the alphabet = string.isalpha()
j = "PerusahaanX"
result_j = j.isalpha()
print(result_j) # True
