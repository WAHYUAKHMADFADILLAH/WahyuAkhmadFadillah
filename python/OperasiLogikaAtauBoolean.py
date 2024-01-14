# not, or, and, xor
# NOT = Kebalikan data awal
# OR = jika ada True maka True
# AND = jika ada False maka False
# XOR = jika beda maka True

# NOT kebalikan dta awal
print('========NOT=======')
a = False
b = False
c = not a
print('data a =',a)
print('--------NOT')
print('c not a=',c)

# OR jika salah satu  hasillnnya true makaa hasilnya true
print('========OR=======')
a = False
b = False
c = a or b
print(a,"OR",b,"=",c)
a = False
b = True
c = a or b
print(a,"OR",b," =",c)
a = True
b = False
c = a or b
print(a,"OR",b," =",c)
a = True
b = True
c = a or b
print(a,"OR",b,"  =",c)

# AND jika dua buah nilai true maka hasilnya true
print('========AND=======')
a = False
b = False
c = a and b
print(a,"AND",b,"=",c)
a = False
b = True
c = a and b
print(a,"AND",b," =",c)
a = True
b = False
c = a and b
print(a,"AND",b," =",c)
a = True
b = True
c = a and b
print(a,"AND",b,"  =",c)

# XOR akan true jika salah satunya true
print('========XOR=======')
a = False
b = False
c = a ^ b
print(a,"XOR",b,"=",c)
a = False
b = True
c = a ^ b
print(a,"XOR",b," =",c)
a = True
b = False
c = a ^ b
print(a,"XOR",b," =",c)
a = True
b = True
c = a ^ b
print(a,"XOR",b,"  =",c)
