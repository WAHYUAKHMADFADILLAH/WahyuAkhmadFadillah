# # membuat gabungan area rentan dari angka

# inputUser = float(input("masukan angka bernilai\nkurang dari 3\ndan\nlebih dari 10 \n:"))

# # +++++++3--------
# # memeriksa nagka kkurang dari 3
# isiKurangDari = (inputUser < 3)
# print("kurang dari 3 =", isiKurangDari)

# # memriksa angka lebih dari 10
# isiLebihDari = (inputUser > 10)
# print("lebih dari 10 =", isiLebihDari)

# # ++++++++3------10+++++++

# isCorrect = isiKurangDari or isiLebihDari
# print('angka yang anda masukan =',isCorrect)

# # -----3+++++++10--------
# # kasus irisan
# print("\n",10*"=","\n")
# inputUser = float(input('masukan angka bernilai \n lebih dari 3\n dan\n kurang dari 10\n:'))

# # ------3+++++++
# # lebih dari 3
# isiLebihDari = inputUser > 3
# print('lebih dari 3 ',isiLebihDari)

# # +++++++10-------
# # kurang dari 10
# isiKurangDari = inputUser < 10
# print("kurang dari 10", isiKurangDari)

# # -----3+++++++10--------
# isCorrect = isiLebihDari and isiKurangDari
# print('angka yang anda masukan', isCorrect)

# soal no 1
# ------0+++++5-----8++++++11-------
print("\n",10*"=","\n")
inputUser=float(input('masukan angka lebih dari 0\nkurang dari 5\ndan\nlebih dari 8\nkurang dari 11\n:'))

# -----0+++++
isiLebihDari0 = inputUser > 0
print("lebih dari 0 :",isiLebihDari0)

# ++++++5------
isiKurangDari5 = inputUser < 5
print('kurang dari 5 :', isiKurangDari5)

# ------8+++++++
isiLebihDari8 = inputUser > 8
print("lebih dari 8 :", isiLebihDari8)

# +++++++11-------
isiKurangDari11 = inputUser < 11
print("kurang dari 11 :",isiKurangDari11)

# ------0+++++5-----8++++++11-------
isCorrect =isiLebihDari0 or isiKurangDari5 and isiLebihDari0 or isiKurangDari11
print("angka yang anda masukan :",isCorrect)

# ===================

# soal no 2
# ++++++0-----5++++++8------11++++++
print("\n",10*"=","\n")
inputUser=float(input('masukan angka kurang dari 0\nlebih dari 5\ndan\nkurang dari 8\nlebih dari 11\n:'))

isiKurangDari0 = inputUser < 0
print("kurang dari 0 :",isiKurangDari0)

isiLebihDari5 = inputUser > 5
print('lebih dari 5 :', isiLebihDari5)

isiKurangDari8 = inputUser < 8
print("kurang dari 8 :", isiKurangDari8)

isiLebihDari11 = inputUser > 11
print("lebih dari 11 :",isiLebihDari11)

# ++++++0-----5++++++8------11++++++
isCorrect =isiKurangDari0 or isiLebihDari5 and isiLebihDari8 or isiLebihDari11
print("angka yang anda masukan :",isCorrect)