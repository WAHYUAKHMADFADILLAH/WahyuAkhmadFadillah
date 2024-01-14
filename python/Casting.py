# casting
# merubah tipe data dari satu tipe data ke  tipe data yang lain
# Tipe data  = int, float, str, bool

## INTEGER
print("=====INTEGER====")
data_int = 9 ;
print("data = ",data_int,",type = ",type(data_int))

data_float = float(data_int) #akan dibulatkan ke bawah
data_str = str(data_int)
data_bool = bool(data_int) #akan false jika nilai integer 0
print("data = ",data_float,",type = ",type(data_float))
print("data = ",data_bool,",type = ",type(data_bool))
print("data = ",data_str,"type = ",type(data_str))

## FLOAT
print("=====FLOAT====")
data_float = 9 ;
print("data = ",data_float,",type = ",type(data_float))

data_int = float(data_float) #akan dibulatkan ke bawah
data_str = str(data_float)
data_bool = bool(data_float) #akan false jjika nilai float 0
print("data = ",data_int,",type = ",type(data_int))
print("data = ",data_bool,",type = ",type(data_bool))
print("data = ",data_str,"type = ",type(data_str))

## BOOLAEAN
print("=====BOOLEAN====")
data_bool = 9 ;
print("data = ",data_bool,",type = ",type(data_bool))

data_int = float(data_bool) #akan dibulatkan ke bawah
data_str = str(data_bool)
data_float = float(data_bool) 
print("data = ",data_int,",type = ",type(data_int))
print("data = ",data_float,",type = ",type(data_float))
print("data = ",data_str,"type = ",type(data_str))

## STRING
print("=====STRING====")
data_str = "wahyu";
print("data = ",data_str,",type = ",type(data_str))

# data_int = float(data_str) #harus angka
data_bool = bool(data_str) #akan flase jika tidak ada isinya
# data_float = float(data_str) 
# print("data = ",data_int,",type = ",type(data_int))
# print("data = ",data_float,",type = ",type(data_float))
print("data = ",data_bool,"type = ",type(data_bool))