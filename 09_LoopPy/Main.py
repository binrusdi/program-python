''' Loop Python  '''
i = 1
while i < 6:
  print(i)
  i += 1
# Break, untuk menghentiksn perulangan meskipun kondisi benar
j = 2
while j < 4:
  print(j)
  if j == 3:
    break
  j += 1
  
# continue, menghentikan program saat ini dan melanjutkan nya
k = 1
while k < 11:
  k += 1
  if k == 5:
    continue
  print(k)
  
# else, untuk menampilkan pesan lain ketika nilai sudah mencapai batasnya
darah = 10
while darah > 2:
  print(f'darah anda, tersisa {darah}')
  darah -= 1
else:
  print('darah anda sudah habis')