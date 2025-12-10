from persediaan import cari_barang


def input_kode_barang():
    while True:
        kode = input("Masukkan Kode barang: ").strip().upper()
        item = cari_barang(kode)
        if item:
            return item
        print("Kode barang salah, coba lagi.")


def input_jumlah_barang(nama_barang):
    while True:
        try:
            jumlah = int(input(f"Jumlah {nama_barang}: "))
            if jumlah >= 1:
                return jumlah
            print("Minimal pembelian 1")
        except ValueError:
            print("Masukkan angka yang valid!")
