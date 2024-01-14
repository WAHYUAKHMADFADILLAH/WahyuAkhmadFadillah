# a = 10, a adalah variable dengan niai 10

# tipe data: Angka Satuan (integer)
data_integer = 1
print("data : ", data_integer)
print("- bertipe :", type(data_integer))

# tipe data: angka dengan koma (float)
data_float = 1.5
print("data : ", data_float)
print("- bertipe :", type(data_float))

# tipe data: Kumpulan Karakter (string)
data_string = "ucup"
print("data : ", data_string)
print("- bertipe :", type(data_string))

# tipe data: True/False (boolean)
data_bool = True
print("data : ", data_bool)
print("- bertipe :", type(data_bool))

# tipe data khusus

# bilangan kompleks
data_komplex = complex(5,6)
print("data : ", data_komplex)
print("- bertipe :", type(data_komplex))

# tipe data dari bahasa C

from ctypes import c_double

data_c_doble = c_double(10.5)
print("data : ", data_c_doble)
print("- bertipe : ", type(data_c_doble))
