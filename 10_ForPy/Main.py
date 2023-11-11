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
# catatan 0enting tentang break
mobil = ['alpart', 'toyota', 'yaris']
for x in mobil:
  if x == 'toyota':
    break # toyota tidak akan dicetak
  print(x)

for y in mobil:
  print(y)
  if y == 'toyota':
    break # toyota akan dicetak