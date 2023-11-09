""" Dictionary Python """
# Kamus digunakan untuk menyimpan nilai data dalam pasangan kunci:nilai.
# Kamus adalah kumpulan yang terurut*, dapat diubah dan tidak mengizinkan duplikat.
# Item kamus disajikan dalam pasangan key:value, dan dapat dirujuk menggunakan key-nya
thisDict = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year' : '1964'
}
print(thisDict)

# Duplikat tidak diizinkan
# Artinya -> kamus tidak boleh memiliki value dengan key yang sama.
# Jika itu terjadi, maka yang terakhir akan menimpa yang sudah ada.

myCar = {
    'brand': 'Toyota',
    'model': 'Avanza',
    'year': 2019,
    'year': 2020
}
print(myCar)

# Menentukan berapa banyak item yang dimiliki dict, gunakan fungsi len().
print(len(myCar))

# Menampilkan tipe data, gunakan fungsi type().
print(type(myCar))

# Membuat ditc dengan konstruktor dict().
myfruits = dict(name='manggo', price=12000, expired='2023')
print(myfruits)

# Akses item pada dict menggunakan key
fruit = myfruits['name']
print(fruit)

# Juga dapat diakses dengan get()
x = myfruits.get('price')
print(x)

# Mendapatkan key yang ada pada dict, gunakan keys()
# Daftar key pada dict, artinya setiap perubahaan yang dilakukan pada kamus akan tercermin pada dalam daftar key
key_dict = myfruits.keys()
print(key_dict)

# Mendapatkan value dengan menggunakan values()
# Dengan ini, values() menampilkan semua dafta value yang ada pada dict
value_dict = myfruits.values()
print(value_dict)

# Mendapatkan semua item dari dict menggunakan items()
# items() akan mengembalikan item dict sebagai tuple dalam daftar
type_tuple = myfruits.items()
print(f'{type_tuple}, ini adalah {type(type_tuple)}')
