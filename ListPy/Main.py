''' List Python  '''
thisList = ['apel', 'tomat', 'semangka']
print(thisList)

print(thisList[0]) # mendapatkan item list dengan index

thisList [0:1] = ['jeruk', 'melon'] # Mengganti rentang 0 s/d 1
print(thisList)

grup_boy = ['angga', 'asep', 'dadang']
grup_boy.insert(2, 'maung') # Menyisipkan item sebelum imdex yang di tentukan
print(grup_boy)

grup_boy.append('love') # Menyisipkan item diakhir daftar
print(grup_boy)

thisList.extend(grup_boy) # menyisipkan item dari daftar lainke daftar saat ini
print(thisList)

grup_boy.remove('asep') # Menghapus item tertentu
print(grup_boy)

grup_boy.pop(1) # Menghapus item dengan index
print(grup_boy)

# Kata kunci del
text = ['kamu', 'kita', 'kami']
del text[2] # Menghapus sesuai index
print(text)
# Jika tanpa index variable nya menjadi undefined

text.clear() # item list menjadi kosong
print(text)

# Iterasi list dengan for
zoo = ['domba', 'sapi', 'keledai']
for hewan in zoo:
  print(hewan)
  
# Iterasi for dengan index
for i in range(len(zoo)):
  print(zoo[i])
  
# Iterasi list sementara dengan while

i = 0
while i < len(zoo):
  print(zoo[i])
  i = i + 1
  
# iterasi paling sederhana
warna = ['merah', 'kuning', 'hijau']
[print(x, end='..') for x in warna]

''' Mengurutkan daftar'''
# Menaik
pelabuhan = ['tanjung priok', 'tanjung perak']
pelabuhan.sort()
print(pelabuhan)

# Menurun
pelabuhan.sort(reverse=True)
print(pelabuhan)

# Menyalin list
list1 = ['krupuk', 'seblak', 'pedas']
list2 = list1.copy()
print(list2)

# Menggabungkan list
# cara ke - 1
makanan = ['bakso', 'soto', 'mie ayam']
level = [1, 2, 3]
launch = makanan + level
print(launch)

#  Cara ke - 2
admin = ['adam', 'azizah', 'viet']
opr = ['angga', 'asep', 'adel']
for name in admin:
  opr.append(name)
print(opr)

# Cara ke - 3
genap = [2, 4, 6]
ganjil = [1, 3, 7]
genap.extend(ganjil)
