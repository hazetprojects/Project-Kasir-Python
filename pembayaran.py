def pembayaran_cash(total):
    total = int(total)  
    print(f"\nTotal yang harus dibayar: Rp {total:,}")

    while True:
        try:
            bayar = int(input("Masukkan uang Anda: Rp "))
            if bayar < total:
                print("Uang tidak cukup, coba lagi.")
            else:
                kembalian = bayar - total
                print(f"Kembalian Anda: Rp {kembalian:,}")
                return bayar, kembalian
        except ValueError:
            print("Masukkan angka yang benar.")