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

