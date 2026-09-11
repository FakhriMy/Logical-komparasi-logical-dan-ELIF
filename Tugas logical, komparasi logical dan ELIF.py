print("== Pengelompokkan usia ==")
usia = int(input ("Masukkan usia kamu: "))

if int(usia <= 12):
    print("Kamu adalah anak-anak!")
elif int(usia <= 17):
    print("Kamu adalah remaja!")
elif int(usia <= 59):
    print("Kamu adalah orang dewasa!")
else:
    print("Kamu adalah lansia!")
print("=========================")
