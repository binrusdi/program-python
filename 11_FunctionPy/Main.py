# Function
'''
- Fungsi adalah sebuah blok kode yang berjalan ketika dipanggil
- Anda dapat meneruskan data, yang di kenal sebagai PARAMETER, ke dalam suatu fungsi
- Suatu fungsi dapat mengembalikan data sebagai hasilnya
'''
# Membuat fungsi dengan keyword def
def myFunction():
    print('Nama saya siganteng')
# Memanggil fungsi
myFunction()

# Argumen / Parameter
# Parameter adalah data yang diteruskan sebagai Argumen
def nama_panjang(fname, lname): # ini parameter
    print(f'nama saya {fname} {lname}')
nama_panjang('dadang', 'faturohman') # ini argumen
# => argumen sering disingkat sebagai "args" dipython

# Jumlah Argumen
'''
- Satu argumen
- Dua argumen
- *args -> argumen berapapun
- Argumen dengan key = value
- **kwargs -> argumen key = value berapapun
'''

# Nilai parameter bawaan
# Jika kita memanggil fungsi tanpa argumen, maka fungsi tersebut akan menggunakan nilai default
def country(state = 'Bandung'): # ini nilau default nya
    print(f'im from {state}')
country('united')
country()

# Data apapun sebagai argumen
# Anda dapat mengirimkan data apapun sebagai argumen dan akan diperlakukan sebagai tipe data yang sama di dalam fungsi
def makanan(food):
    for x in food:
        print(x)

seafood = ['cumi', 'kakap', 'lobster']
makanan(seafood)

# Return nilai
# Untuk membiarkan suatu fungsi mengembalikan nilai, gunakan keyword 'return'
def hello():
    return 'Selamat pagi'
print(hello())








