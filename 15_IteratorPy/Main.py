# Iterator adalah object berisi sejumalh nilai yg dapat dihitung
'''
Secara teknis dalam python, iterator adalah object yang mengimplementasikan protokol iterator,
yang terdiri dari metod __iter__() dan __next__().
'''
# Kmebalikan iterator dari tuple, dan cetak setiap nilai
mytuple = ('apple', 'banana', 'cherry')
myiter = iter(mytuple)
print(next(myiter))
print(next(myiter))
print(next(myiter))

# Bahkan string merupakan object yang dapat diubah, berisi rangkaian karakter
mystr = 'banana'
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# Perulangan melalui iterator
mytup = ('yaris', 'avanza', 'agya')
for x in mytup:
    print(x)
# Perulangan for sebenarnya membuat objek iterator dan mengeksekusi metode next() untuk setiap perulangan.

# Buat iterator
class Number:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x
    
myclass = Number()
myiter = iter(myclass)

print(next(myiter))
# for x in myiter:
#     print(x) # iterasi ini tidak adkan berhenti

# Menghentikan iterasi
class MyNumber:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
        
mykelas = MyNumber()
myitter = iter(mykelas)
for x in myitter:
    print(x)

