# operasi aritmatika

a = 10
b = 3

# operasi tambah + 
hasil = a + b
print (a,'+',b,'=',hasil)

# operasi pengurangan -
hasil = a - b
print (a,'-',b,'=',hasil)

# operasi perkalian * 
hasil = a * b
print (a,'*',b,'=',hasil)

# operasi pembagian
hasil = a / b
print (a,'/',b,'=',hasil)

# operasi ekponen pangkat **
hasil = a ** b
print (a,'**',b,'=',hasil)

# operasi modulus
hasil = a % b
print (a,'%',b,'=',hasil)

# operasi flor division
hasil = a // b
print (a,'//',b,'=',hasil)

# prioritas operasi, operational precedence
'''
    1. ()
    2. eksponen **
    3. perkalia dan teman teman * / ** % z//
    4. pertambahan dan pengurangan
'''
x = 10
y = 5
z = 2

hasil = (x + z) * y / z // x - z * z
print('(',x,'+',z,')','*',y,'/',z,'//',x,'-',z,'*',z,'=',hasil)