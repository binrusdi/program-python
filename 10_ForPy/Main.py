''' For Python '''
'''
Perulangan for digunakan untuk mengulangi suatu urutan(list, tuple, dict, set,
dan string)
'''

# String
nama = "rusdiana"
for chart in nama:
  print(chart)
  
# list
fruits = ['pisang', 'cherry', 'apel']
for fruit in fruits:
  print(fruit)
  
# for bisa di tambahkan dengan break atau continue
# catatan penting tentang break
mobil = ['alpart', 'toyota', 'yaris']
for x in mobil:
  if x == 'toyota':
    break # toyota tidak akan dicetak
  print(x)

for y in mobil:
  print(y)
  if y == 'toyota':
    break # toyota akan dicetak

# range()
data_range = range(20, 100, 2) # dimulai dari 20 s/d angka 100 tp kecualikan, nilai 2 adalah kelipatan yang akan ditambhakan
for data in data_range:
  print(data, end=',')

# else pada for
for x in range(6):
  print(x)
else:
  print('Nilai melebihi angka yang ditentukan')

# else tidak akan dieksekusi jika ada break di atas nya
for z in range(11):
  if z == 7: break
  print(z)
else:
  print('finally finished')

# Nested Loop
# "Loop dalam" akan di eksekusi satu kali setiap iterasi "Loop luar"
adj = ['merah', 'besar', 'lezat']
buah = ['apel', 'pisang', 'cheri']
for x in adj:
  for y in buah:
    print(x, y)

# latihan
artikel = ['coverall hitam', 'coverall olive', 'coverall khaki']
size = ['s', 'm', 'l', 'xl', 'xxl']
for art in artikel:
  for sz in size:
    print(art, sz)

# pass pada for loop
# for loop tidak boleh kosong, untuk menghindari kesalahan tambahkan pass ketika for tidak membutuhkan konten
for x in [0, 1, 2]:
  pass