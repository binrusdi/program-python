''' Kondisi dan if pada Python '''
'''
a == b,
a != b,
a < b,
a > b,
a <= b,
a >= b,
'''
# Jika kondisi true
a = 23
b = 200
if a < b:
  print('\nHello ucup\n')

# Jika kondisi False
if a > b:
  print('Hello ucup')
elif a < b:
  print('\tHello otong')
  
# Menangkap apapu yang tidak tertangkap oleh if atau elif
b = 10
c = 15
if b > c:
  print('itu benar')
elif b == c:
  print('benar juga')
else:
  print('''
  Ini paling benar, karna b tidak lebih besar dari c, dan b tidak sama
  dengan c''')
  
# Syntak ternary
buah = 'mangga'
# if
if buah: print('Makanan kesukaanku')
# if else
print('Makanan kesukaan') if buah == False else print('Mungkin buah mangga')
