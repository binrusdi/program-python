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

# Memeriksa key, apakah ada di dalam dict menggunakan in
if 'name' in myfruits:
    print('yes, "name" is one keys in the dictionaries')

# Anda dapat mengubah nilai item dengan mengacu pada nama key nya.
biodata = {
    'nama': 'Rusdiana',
    'alamat': 'Cihideung',
    'tanggal_lahir': '28 Mei 1994',
}
biodata['alamat'] = 'Lembur Sawah'
print(biodata)

# Memperbaharui dict dengan menggunakan update()
# Method ini akan meperbaharui kamus dengan item dari argumen yang diberikan
# Argumen nya harus berupa dict atau object yang dapat diubah dengan pasangan key:value
alamat = {
    'jalan': 'pangalengan',
    'desa': 'tribaktimulya',
    'kec': 'pangalengan',
}
alamat.update({'jalan': 'pangalengan-banjaran'})
print(alamat)

# Menambhakan item pada dict
alamat['rt'] = '04'
alamat['rw'] = '06'
print(alamat)

# Menghapus dengan beberapa method
# pop() -> menghapus dengan item yang ditentukan
alamat.pop('jalan')
print(alamat)
# popitem() -> menghapus item terakhir yang dimasukan
alamat.popitem()
print(alamat)
# clear() -> mengosongkan item saja
alamat.clear()
print(alamat)
'''
# del -> menghapus item dengan nama key yang di tentukan, juga dapat menghapus seluruh dict
del alamat['kec']
print(alamat)
del alamat
print(alamat) # NameError: name 'alamat' is not defined karna dict nya sudah tidak ada
'''
# Mengiterasi dict dengan for
karyawan = {
    'pria': 'angga',
    'perempuan': 'citra',
}
for kunci, nilai in karyawan.items():
    print(f'{kunci} diwakili oleh {nilai}')

# Menyalin dict dengan method copy()
salinan_dict = karyawan.copy()
print(salinan_dict)

# Cara lain untuk menyalin dict dengan menggunakan, construktor dict()
salin_again = dict(salinan_dict)
print(salin_again)

# Dict bersarang
# cara ke -1
myfamily = {
    'child1': {
        'name': 'Ahmda',
        'year': '2023'
    },
    'child2': {
        'name': 'Agus',
        'year': '2021'
    }
}
print(myfamily)
# cara ke -2
toyota = {
    'model': 'Avanza',
    'year': '2019'
}
honda = {
    'model': 'yaris',
    'year': '2020'
}
mobil = {
    'merek_1': toyota,
    'merek_2': honda
}

print(mobil)
