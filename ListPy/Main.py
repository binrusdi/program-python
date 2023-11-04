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