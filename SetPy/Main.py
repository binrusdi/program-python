''' Set Python '''
# Satu set adalah koleksi yang unordered, unchangeable*, dan unindexed.
# Item tang di tetapkan tidak dapat diubah, tapi dapat dihapus dan ditambahkan item baru
# Duplikat tidak diizinkan
thisset = {'x', 'y', 'z'}
print(thisset)

# Mengakses item hanya dengan iterasi
set_mobil = {'toyota', 'honda', 'suzuki'}
for merk in set_mobil:
  print(merk)
  
# Menambah item di set
set_mobil.add('datsun')
print(set_mobil)

# Menambah kan set lain ke set saat ini.
thisset.update(set_mobil)
print(thisset)

# Hapus item pada set.
set_mobil.remove('honda')
print(set_mobil)
set_mobil.discard('toyota')
print(set_mobil)

# mengembalikan item yang di Hapus
orang = {'tinggi', 'pendek', 'gemuk'}
orang.pop()
print(orang)

# Mengosongkan set
ty_set = {'kamu', 'dia', 'dirinya'}
ty_set.clear()
print(ty_set)

# Menghapus set dengan keyword del