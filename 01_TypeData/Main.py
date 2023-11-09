''' Type data bawaan python '''
'''
Jenis teks => str
Jenis numerik => int, float, complex
Jenis urutan => list, tuple, range
Jenis pemetaan => dict
Jenis set => set, frozenset
Jenis boolean => bool
Jenis biner => bytes, bytearray, memoryview
Tidak ada jenis => typeNone
'''

''' Mengatur type data '''
'''
x = 'Hello world' # str
x = 20 # int
x = 20.5 # float
x = 1j # complex
x = ['pisang', 'semangka', 'anggur'] # list
x = ('sirsak', 'durian', 'melon') # tuple
x = range(6) # range
x = {'nama': 'Rusdiana', 'age': 29} # dict
x = {'apple', 'banana', 'cherry'} # set
x = ({'apple', 'banana', 'cherry'}) # frozenset
x = True # bool
x = b'Hello' # bytes
x = bytearray(5) # bytearray
x =  memoryview(bytes(5)) # memoryview
x = None # NoneType
'''

''' Mengatur type data tertentu '''
''' Menggunakan fungsi konstruktor '''
'''
x = str() # str
x = int() # int
x = float() # float
x = complex() # complex
x = list(()) # list
x = tuple(()) # tuple
x = range() # range
x = dict(key = value, key = value) # dict
x = set(()) # set
x = frozenset(()) # frozenset
x = bool() # bool
x = bytes() # bytes
x = bytearray() # bytearray
x = memoryview(bytes()) # memoryview
'''