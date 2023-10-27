"""Memamhami List lebih dalam"""

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
