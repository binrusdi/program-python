# Variable Scoop
''' Variable hanya tersedia dalam wilayah pembuatannya '''

# Lingkup "Lokal"
''' Varaible yang dibuat di dalam fungsi dan hanya dapat digunakan di dalam fungsi itu sendiri '''
def myfunc():
    x = 300
    print(x)
myfunc()

# Lingkup "Global"
y = 200
def number():
    print(y)
number()