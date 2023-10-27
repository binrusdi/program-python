"""Memahami List lebih dalam"""

# List dapat diindex dan diiris
fruit = ["mangga", "apel", "stroberi"]
print(len(fruit))  # len() return field items in list
print(fruit[0])  # [index-n] return item from index-n
print(fruit[:1])  # slicing item from first item to index-1 as lastend

# List dapat memiliki operasi gabungan
sayuran = ["bayam", "wortel", "tomat"]
print(fruit + sayuran)

# List dapat diubah isi nya
sayuran[1] = "pakcoy"
print(sayuran)

# List dapat digabungkan
makanan_pokok = sayuran + fruit
print( makanan_pokok )

# List dapat diubah isinya
puluhan = [10, 25, 30, 45]
print(puluhan)
puluhan[2] = 9**2
print(puluhan)

# Menambahkan item baru di akhir list dengan method .append()
tools = ["garpu", "sendok"]
tools.append("baskom")
print(tools)

# Menhapus beberapa nilai dengan irisan
tools[:1] = ["serok"]
print(tools)

# Membersihkan item dengan irisan
tools[:] = []
print(tools)

# Method len() juga berlaku untuk list
nama = ["Rusdiana", "Angga", "Asep"]
print(len(nama))

# Menyusun list (Membuat daftar didaftar lain)
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
x = [a, b]
print(x)
print(len(x))
print(x[1][2])