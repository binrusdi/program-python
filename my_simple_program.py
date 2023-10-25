# Fungsi untuk penjumlahan
def tambah(x, y):
    return x + y

# Fungsi untuk pengurangan
def kurang(x, y):
    return x - y

# Fungsi untuk perkalian
def kali(x, y):
    return x * y

# Fungsi untuk pembagian
def bagi(x, y):
    if y == 0:
        return "Tidak dapat dibagi dengan 0"
    return x / y

while True:
    # Menampilkan menu
    print("Pilih operasi:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Keluar")

    # Meminta input dari pengguna
    pilihan = input("Masukkan nomor operasi (1/2/3/4/5): ")

    # Keluar dari program jika pengguna memilih 5
    if pilihan == '5':
        print("Keluar dari program.")
        break

    if pilihan not in ('1', '2', '3', '4'):
        print("Pilihan tidak valid. Silakan coba lagi.")
        continue

    num1 = float(input("Masukkan angka pertama: "))
    num2 = float(input("Masukkan angka kedua: "))

    if pilihan == '1':
        print("Hasil penjumlahan:", tambah(num1, num2))
    elif pilihan == '2':
        print("Hasil pengurangan:", kurang(num1, num2))
    elif pilihan == '3':
        print("Hasil perkalian:", kali(num1, num2))
    elif pilihan == '4':
        print("Hasil pembagian:", bagi(num1, num2))
