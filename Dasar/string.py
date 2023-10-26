""" Membahas lebih dalam tentang string """

str_kutip_satu = 'String bisa diberikan dengan TANDA KUTIP SATU (\')'
print(str_kutip_satu)

print("\n")  # Hiraukan ini jika anda melihat di code editor

str_kutip_dua = "String juga bisa diberikan dengan TANDA KUTIP DUA (\")"
print(str_kutip_dua)

print("\n")  # Hiraukan ini jika anda melihat di code editor

str_kutip_tiga = """
String juga bisa diberikan dengan TANDA KUTIP TIGA (\"\"\")
"""
print(str_kutip_tiga)

""" String dalam python dapat di index, urutan pertama adalah 0 """

karakter = "karakter"
print(f"Jumlah karakter menggunakan len() yaitu {len(karakter)}")

print("\n")  # Hiraukan ini jika anda melihat di code editor

# Cara menghitung index string pada python yaitu, setiap karakter dibungkus oleh sebuah pembatas kiri kanan, pembatas kiri di awal karakter itu index 0, sedangkan pembatas setelah karakter itu index 1. Jika hanya satu karakter.
"""
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
"""
print(karakter[0:])  # mengambil hurup pertama sampai akhir
print(karakter[:4])  # mengambil karakter sampai index ke 4
