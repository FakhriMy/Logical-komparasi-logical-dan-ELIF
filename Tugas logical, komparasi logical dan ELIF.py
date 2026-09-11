print("== Pengelompokkan usia ==")
usia = int(input ("Masukkan usia kamu: "))

if usia < 1:
    print("Invalid")
elif usia <= 12:
    print("Kamu adalah anak-anak")
elif usia <= 17:
    print("Kamu adalah remaja!")
elif usia <= 59:
    print("Kamu adalah orang dewasa!")
else:
    print("Kamu adalah lansia!")
print("=========================")
