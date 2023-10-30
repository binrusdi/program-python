""" While """
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a + b
"""
    1, 1  = 1, 0 + 1
    1, 2  = 1, 1 + 1
    2, 3  = 2, 1 + 2
    3, 5  = 3, 2 + 3
    5, 8  = 5, 3 + 5
    8, 13 = 8, 5 + 8

    cara menghitung pibonanci di belakang layar
"""
# => Argumen kata kunci end didalam method print() menghindari baris baru pada output, atau mengakhiri output dengan sting yang berbeda
c, d = 0, 1
while a < 1000:
    print(a, end=",")
    a, b = b, a + b


""" Pernyataan IF """
print("\n")
"""
nilai = int(input("Please input nilai dengan integer/angka : "))

if nilai >= 70:
    print("Nilai nya terlalu besar")
elif nilai <= 20:
    print("Nilai terlalu kecil")
elif nilai == 50:
    print("Nilai nya pas dengan yang diharapkan")
else:
    print("Tidak mendekati")
"""

# Pernyataan FOR
# for pada python berbeda dengan bahasa programan lain

# iterasi list dan mendapatkan panjang dari karakter, item pada list
hewans = ["Kucing", "Singa", "Meong"]
for hewan in hewans:
    print(hewan, len(hewan))

# Mengulang salinan koleksi sambil mengubahnya
users = {
    "hans": "active",
    "jhons": "inactive",
    "melly": "active"
}
# mengulangi salinan
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
# buat koleksi baru
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
print(active_users)

""" FUNGSI """

# Mengulangi serangkaian angka dengan range()
# Rumus -> range(start, rentang, kenaikan)
# endpoit tidak pernah dilibatkan dalam serangkaian iterasi
for i in range(5):
    print(i)

range(5, 10)  # jangan digunakan
r = range(5, 10)  # jangan digunakan

# Membuat list dengan range
lr = list(range(2, 10))
print(lr)

# Dengan menambahkan aturan kenaikan
ll = list(range(3, 15, 5))
print(ll)


# Break dan Continue
# Pernyataan break keluar dari for loop dan while loop terdalam
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')