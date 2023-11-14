''' Class dan Object '''
'''
Di python hampir semua nya object dengan property dan methodnya sendiri
'''
# Buat class, gunakan keyword "class"
class MyClass:
  x = 5
# Buat object
p1 = MyClass()
print(p1.x)
# Diaras adalah penerapan object sederhana

# fungsi __init__()
'''
Gunakan fungsi __init__() untuk menetapkan nilai pd properti object, atau
operasi lain yang perlu dilakukan saat object dibuat.
'''
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
p1 = Person('Jhon', 36)
print(p1.name)
print(p1.age)
# fungsi __init__() dipanggil otomatis setiap kali class dipanggil untuk membuat object baru.

# fungsi __str__()
'''
fungsi __str__() mengontrol apa yang harus dikembalikan ketika object kelas
direpresentasikan sbg string.
jika fungsi __str__() tidak disetel, representasi string object akan
dikembalikan
'''
# Representasi string suatu objek DENGAN fungsi __str__():
class Orang:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def __str__(self):
    return f'{self.name} is {self.age}'
    
p2 = Orang('ucup', 29)
print(p2)
  
# Method object
class Mobil:
  def __init__(self, merk, warna):
    self.merk = merk
    self.warna = warna
  
  def __str__(self):
    return f'{self.merk} {self.warna}'
  
  def maju(self):
    print(f'mobil {self.merk} yang berwarna {self.warna} melaju dengan kencang')
    
yaris = Mobil('Honda', 'Red')
yaris.maju()
# parameter 'self' adakah referensi ke instance kelas saat iini
# dan digunakan untuk mengakses variable milik kepas tsb
# tidak harus diberi nama 'self', tapi penempatan nya harus jd parameter pertama

# Ubah property object
class Penumpang:
  def __init__(self, nama, no):
    self.nama = nama
    self.no = no

  def beli(self):
    print(f'{self.no} adalah no duduk penumpang bernama {self.nama}')

ahmad = Penumpang('ahmad', 20)
ahmad.beli()
ahmad.nama = 'yusuf' # ubah properti object
ahmad.no = 25 # ubah properti object
ahmad.beli()
del ahmad.no
ahmad.beli()