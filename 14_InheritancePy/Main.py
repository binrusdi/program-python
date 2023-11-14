# Python Inheritance
# class induk
class Person:
  def __init__(self, firstname, lastname):
    self.firstname = firstname
    self.lastname = lastname
    
  def printname(self):
    print(f'{self.firstname} {self.lastname}')

x = Person('Muhammad', 'ihsan')
x.printname()

# class anak
class Student(Person): # class induk dijadikan parameter
  pass

y = Student('Otong', 'Surotong')
y.printname()

# Tambah fungsi __init__()
class Student(Person):
  def __init__(self, fname, lname): # jika hanya ini pewarisan dari induk hilang
    Person.__init__(self, fname, lname) # mempertahankan pewarisan dari induk

z = Student('Assasin', 'cread')
z.printname()

# mengganti nama class induk dengan fungsi super()
class Book:
  def __init__(self, namebook, pagesbook):
    self.namebook = namebook
    self.pagesbook = pagesbook
  
  def printbook(self):
    print(
    f'judul buku adalah {self.namebook} dengan mempunyai {self.pagesbook} halaman'
    )

judul = Book('Safinah', 200)
judul.printbook()

class Judul(Book):
  def __init__(self, namebook, pagesbook, year):
    super().__init__(namebook, pagesbook) # nama class Book, diganti dengan "super"
    self.graduation = year

  def printtahun(self):
    print(f'tahun di cetak {self.graduation}')

tijan = Judul('tijan', 500, 1920)
tijan.printbook()
tijan.printtahun()