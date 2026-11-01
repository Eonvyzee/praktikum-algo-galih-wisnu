
nama_bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli",
              "Agustus", "September", "Oktober", "November", "Desember"]

ulang = "y"
while ulang.lower() == "y":
   
    bulan = int(input("Masukkan bulan (1-12): "))
    while bulan < 1 or bulan > 12:
        print("Bulan tidak valid! Harus antara 1 sampai 12.")
        bulan = int(input("Masukkan bulan (1-12): "))

    
    tahun = int(input("Masukkan tahun: "))
    while tahun < 1:
        print("Tahun tidak valid! Harus bilangan positif.")
        tahun = int(input("Masukkan tahun: "))

   
    if bulan in (1, 3, 5, 7, 8, 10, 12):
        hari = 31
    elif bulan in (4, 6, 9, 11):
        hari = 30
    else:  # Februari
        if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
            hari = 29      # tahun kabisat
        else:
            hari = 28

    print(f"Bulan {nama_bulan[bulan-1]} tahun {tahun} memiliki {hari} hari.")
    ulang = input("Hitung lagi? (y/t): ")

print("Program selesai.")
