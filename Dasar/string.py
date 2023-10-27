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
print(f"Menampilkan jumlah karakter menggunakan len()\n dimana variable karakter = \"karakter\" adalah berjumlah {len(karakter)}")

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
print('\n')
# Keunikan string menggunakan IS yang mengembalikan boolean, tapi tanda baca itu menghasilkan false

a = 'linux'
b = 'linux'

print( 'a = \' linux \'' )
print( 'b = \' linux \'' )

print( 'a is b' )
print(a is b)

# Escape di python
"""
\newline	Ignored
\\	Backslash (\)
\'	Single quote (')
\"	Double quote (")
\a	ASCII Bell (BEL)
\b	ASCII Backspace(BS)
\f	ASCII Formfeed (FF)
\n	ASCII Linefeed (LF)
\N{name}	Character named name in the Unicode database (Unicode only)
\r	ASCII Carriage Return (CR)
\t	ASCII Horizontal Tab (TAB)
\uxxxx	Character with 16-bit hex value xxxx (Unicode only)
\Uxxxxxxxx	Character with 32-bit hex value xxxxxxxx (Unicode only)
\v	ASCII Vertical Tab (VT)
\ooo	Character with octal value ooo
\xhh	Character with hex value hh
"""