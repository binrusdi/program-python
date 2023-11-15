# String Python
# => gunakan fungsi print(). untuk mencetak isi variable
# Menetapkan string ke variable
string_kutip_satu = 'Ini adalah string' # ini adalah string
string_kutip_dua = "Ini juga adalah string dengan kutip dua" # Ini juga adalah string dengan kutip dua
string_multi_baris = '''Ini adalah string multi baris,
yang mana jika di enter tidak akan error.
dan penampakan nya dalam console,
akan sesuai dengan apa yang di tulis di code. dan multi baris ini menggunakan kutip 3'''

# String adalah Array
'''
String pada python adalah array byte yang mewakili karakter unicode, namun python tidak mempunyai tipe data karakter.
Karakter tunggal hanyalah sebuah string dengan panjang 1.
Tanda kurung siku dapat digunakan untuk mengakses element string.
'''
a = "Hello"
print(a[0]) # H

# Perulangan melalui sttring
b = "Banana"
for char in b:
    print(char) # B a n a n a (vertikal)

# Panjang string
c = "Hello, world"
print(len(c)) # 12

# Periksa string menggunakan in
# => Mengembalikan boolean
d = "Hello, world"
print("world" in d) # True

# Periksa string menggunakan if
e = "Mobil itu bermerk yaris"
if "yaris" in e:
    print("Ya, mereknya adalah 'yaris'") # Ini akan dicetak

# Periksa string dengan not in
f = "Iron man adalah pahlawan marvel?"
print("Iron man" not in f) # False

# Mengembalikan serangkaian karakter dengan mengiris
# => tentukan index awal dan akhir, pisahkan dengan titik dua
g = "World"
print(g[0:]) # World
print(g[0:3]) # Wor
print(g[:len(g)]) # World

# Escape Character
'''
Untuk menyisipkan karakter ilegal dalam sebuah string, gunakan escape karakter.
Karakter escape adalah garis miring terbalik \ yang diikuti dengan karakter yg ingin disisipkan.
'''
# \'
txt_1 = 'It\'s alright'
print(txt_1) # It's alright

# \\
txt_2 = "This will insert one \\ (backslash)."
print(txt_2) # This will insert one \ (backslash).

# \n
txt_3 = "Hello\nWorld"
print(txt_3) # Hello
             # World

# \r
txt_4 = "Hi\rrusdi"
print(txt_4)