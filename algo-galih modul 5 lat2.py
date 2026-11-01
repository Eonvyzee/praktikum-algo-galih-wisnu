
total = 0.0

while True:
    umur = input("masukkan umur: ")
    if umur == "":
        break
    umur = int(umur)

    if umur <= 2:
        harga = 0
        print("Gratis")
    elif 3 <= umur <= 12:
        harga = 14
        print("Harga $14.00")
    elif umur >= 65:
        harga = 18
        print("Harga $18.00")
    else:
        harga = 23
        print("Harga $23.00")

    total = total + harga
    print("Running total: %.2f" % total)

uang = float(input("masukkan jumlah uang: "))
while uang < total:
    print("Uang kurang $%.2f, masukkan lagi" % (total - uang))
    uang = float(input("masukkan jumlah uang: "))

print("Running kembalian: %.2f" % (uang - total))

total = 0.0

while True:
    umur = input("masukkan umur: ")
    if umur == "":
        break
    umur = int(umur)

    if umur <= 2:
        harga = 0
        print("Gratis")
    elif 3 <= umur <= 12:
        harga = 14
        print("Harga $14.00")
    elif umur >= 65:
        harga = 18
        print("Harga $18.00")
    else:
        harga = 23
        print("Harga $23.00")

    total = total + harga
    print("Running total: %.2f" % total)

uang = float(input("masukkan jumlah uang: "))
while uang < total:
    print("Uang kurang $%.2f, masukkan lagi" % (total - uang))
    uang = float(input("masukkan jumlah uang: "))

print("Running kembalian: %.2f" % (uang - total))
