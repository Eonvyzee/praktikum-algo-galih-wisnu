# Latihan Pertama: Rata-rata nilai berdasarkan huruf mutu (Exercise 66)
def nilai_huruf(huruf):
    tabel = {
        "A": 4.00, "A-": 3.75,
        "B+": 3.50, "B": 3.00, "B-": 2.75,
        "C+": 2.50, "C": 2.00, "C-": 1.75,
        "D": 1.50, "E": 1.25,
    }
    return tabel.get(huruf)


def hitung_rata_rata():
    total = 0
    jumlah = 0
    while True:
        huruf = input("masukkan nilai: ").strip().upper()  # huruf kecil diubah jadi kapital
        if huruf == "":
            break
        angka = nilai_huruf(huruf)
        if angka is None:
            print("nilai tidak valid, ulangi")
        else:
            print("nilai =", angka)
            total = total + angka
            jumlah = jumlah + 1
    if jumlah > 0:
        print("rata - rata nya adalah: ", total / jumlah)
    else:
        print("tidak ada nilai yang dimasukkan")


hitung_rata_rata()
