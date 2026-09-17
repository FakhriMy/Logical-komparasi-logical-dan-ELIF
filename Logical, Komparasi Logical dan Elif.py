# Program 4.1 Logical
# Operasi logika atau boolean
# not, or, and, xor

# NOT (kebalikan dari nilai)
print("==== NOT ====")
a = True
b = not a
print("data a =", a)
print("--------- NOT")
print("data b =", b) 

# OR (jika salah satu True maka hasilnya True)
print("==== OR ====")
a = False
b = False
c = a or b
print(a, "OR", b, "=", c)
a = False
b = True
c = a or b
print(a, "OR", b, "=", c)
a = True
b = False
c = a or b
print(a, "OR", b, "=", c)
a = True
b = True
c = a or b
print(a, "OR", b, "=", c)

# AND (jika dua buah nilai True maka hasilnya True)
print("==== AND ====")
a = False
b = False
c = a and b
print(a, "AND", b, "=", c)
a = False
b = True
c = a and b
print(a, "AND", b, "=", c)
a = True
b = False
c = a and b
print(a, "AND", b, "=", c)
a = True
b = True
c = a and b
print(a, "AND", b, "=", c)

# XOR (akan true jika salah satu True dan yang lain False)
print("==== XOR ====")
a = False
b = False
c = a ^ b
print(a, "XOR", b, "=", c)
a = False
b = True
c = a ^ b
print(a, "XOR", b, "=", c)
a = True
b = False
c = a ^ b
print(a, "XOR", b, "=", c)
a = True
b = True
c = a ^ b
print(a, "XOR", b, "=", c)

# Program 4.2 logikal dan komparasi
# Membuat gabungan area rentang dari angka 5 - 15
# ++++++5------15++++++
print("==================================")
input_user = float(input("Masukan angka yang bernilai \nlebih dari 5 \natau \nkurang dari 15\n= "))
# ++++++5------
# angka kurang dari 5
kurang_dari_5 = (input_user < 5)
print("Kurang dari 5 =", kurang_dari_5)

# ------15++++++
# angka lebih dari 15
lebih_dari_15 = (input_user > 15)
print("Lebih dari 15 =", lebih_dari_15)
Benar = (kurang_dari_5 or lebih_dari_15)
print("Angka anda  =", Benar)

print("=================================")
# ------5+++++++15-----
# kasus irisan
print("=================================")
input_user = float(input("Masukan angka yang bernilai \nlebih dari 5 \ndan \nkurang dari 15\n= "))
# ------5++++++
# angka lebih dari 5
lebih_dari_5 = (input_user > 5)
print("Lebih dari 5 =", lebih_dari_5)

# ++++++15------
# angka kurang dari 15
kurang_dari_15 = (input_user < 15)
print("Kurang dari 15 =", kurang_dari_15)
Benar = (lebih_dari_5 and kurang_dari_15)
print("Angka anda  =", Benar)

print("=================================")
# Program 4.3 IF and ELSE
# if dan else statement
# 1. if nya
# 2. kondisi
# 3. aksi
print("=================================")
nama = input("Siapa nama anda? ")

# 1. Program if inline
if nama == "ucup": print("Hai Ucup")
print("Akhir dari program if inline")

# 2. Program if indentation
if nama == "ucup":
    print("Hai Ucup")
    print("Apa kabar?")
print("Akhir dari program if indentation")

# 3. Else statement
if nama == "Bayu":
    print("Hai Bayu")
else:
    print("siapa kamu?")
print("Akhir dari program if else statement")
print("=================================")

# Program 4.4 Elif statement
print("=================================")
nama = input("Siapa nama anda? ")
# if kondisi:
#     aksi true
# elif kondisi:
#     aksi true
# elif kondisi:
#     aksi true
# else:
#     aksi

if nama == "cupsky": #kondisi 1
    print("Hai cupsky") #aksi true 1
elif nama == "Daffa": #kondisi 2
    print("Hai Daffa") #aksi true 2
elif nama == "Hanif": #kondisi 3
    print("Hai Hanif") #aksi true 3
else: 
    print("siapa kamu?") #aksi false
print("Akhir dari program if elif else statement")
print("=================================")