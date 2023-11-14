# lambda
# fungsi lambda adalam fungsi anonim
# lambda dapat menerima beberapa argumen tapi hanya satu ekspresi
x = lambda a, b : a * b
print(x(5, 6))

# Mengapa menggunakan fungsi 'lambda'
'''
Kekuatan fungsi lambda ditampiljan lebih baik saat anda menggunakan sbg fungsi
anonim di dalam fungsi lain.
'''
def myfunct(n):
  return lambda a : a * n
mydouble = myfunct(2) # argumen untuk nilai n
print(mydouble(11)) # argumen untuk nilai a