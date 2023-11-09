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
# Menggabungkan type data set dengan union()
set_1 = {'a', 'b', 'c'}
set_2 = {1, 2, 3}
set_3 = set_1.union(set_2)
print(set_3)
# Menggabungkan type data set dengan update()
set_1.update(set_2)
print(set_1)

# Simpan hanya item duplikat dari dua set
x = {'apple', 'banana', 'cherry'}
y = {'microsoft', 'google', 'apple'}
x.intersection_update(y)
print(x) # {'apple'}

# Simpan semua, tapi bukan duplikatnya
a = {'mobil', 'motor', 'pesawat'}
b = {'darat', 'pesawat', 'udara'}
a.symmetric_difference_update(b)
# Catatan: Nilai True and 1dianggap sebagai nilai yang sama dalam kumpulan, dan diperlakukan sebagai duplikat:
print(a) # {'udara', 'darat', 'mobil', 'motor'}

""" Method Set """
"""
Method	            Description
add()	              Adds an element to the set
clear()	            Removes all the elements from the set
copy()	            Returns a copy of the set
difference()	      Returns a set containing the difference between two or more sets
difference_update()	Removes the items in this set that are also included in another, specified set
discard()	          Remove the specified item
intersection()	    Returns a set, that is the intersection of two other sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	      Returns whether two sets have a intersection or not
issubset()	        Returns whether another set contains this set or not
issuperset()	      Returns whether this set contains another set or not
pop()	              Removes an element from the set
remove()	          Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	            Return a set containing the union of sets
update()	          Update the set with the union of this set and others
"""