print(''' <==Tuple Python ==>
# Tuple adalah koleksi yang terurut dan tidak dapat diubah.
# Tuple di tulis dengan tanda kurung bulat ()
# Tuple itemnya diindex dan bisa duplikat
''')
ThisTuple = ('banana', 'apple', 'manggo')
print(ThisTuple)

# Buat tuple dengan satu item, tapi harus di akhiri dengan koma dibelakang item.
satu_item = ('angga',)
print(satu_item, type(satu_item))

# Tuple dapat mencampur type data
mix = ('mangga', 20, True)
print(mix, type(mix))

# Akses tuple
print(mix[1])

# Tidak dapat diubah, ditambah, dan dihapus. tapi bisa di akali dengan mengkonversi ke list dan di ubah kembali ke tuple

# Menambahkan tuple dari tuple
tuple_1 = ('merah', 'kuning', 'hijau')
biru = ('biru',)
tuple_1 += biru
print(tuple_1)

# Membongkar tuple
fruit = ('jeruk', 'nanas', 'mangga')
(jeruk, nanas, mangga) = fruit
print(jeruk, type(jeruk))
print(nanas, type(nanas))
print(mangga, type(mangga))

# Menambahkan bintang(*) di awal nama variable untuk memasukan item bongkaran tuple yang tersisa
mobil = ('avanza', 'yaris', 'brio')
(toyota, *honda) = mobil
print(toyota, type(toyota))
print(honda, type(honda))

# Loop tuple sama dengan kumpulan data yg lain seperti list