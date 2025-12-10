from input_barang import input_kode_barang, input_jumlah_barang

def tampil_keranjang(keranjang):
    if not keranjang:
        print("\n=== Keranjang Saat Ini: (kosong) ===\n")
        return

    print("\n=== Keranjang Saat Ini ===")
    print(f"{'Barang':<30} {'Harga':>10} {'Jumlah':>8} {'Subtotal':>15}")
    print("-" * 72)

    for item in keranjang:
        kode, nama, harga, jumlah = item
        subtotal = harga * jumlah

        harga_str = f"Rp {harga:,}"
        subtotal_str = f"Rp {subtotal:,}"

        print(f"{nama:<30} {harga_str:>10} {jumlah:>8} {subtotal_str:>15}")

    print("-" * 72)


def tambah_barang(keranjang, item, jumlah):
    for isi in keranjang:
        if isi[0] == item[0]:
            isi[3] += jumlah
            return f"Jumlah {item[1]} ditambah {jumlah}"
    keranjang.append([item[0], item[1], item[2], jumlah])
    return f"{item[1]} ditambahkan ke keranjang"


def ubah_jumlah(keranjang):
    if not keranjang:
        return "Keranjang kosong, tidak ada yang bisa diubah."

    kode = input("Masukkan kode barang yang ingin diubah jumlahnya / dihapus : ").strip().upper()
    for item in keranjang:
        if item[0] == kode:
            while True:
                new = input(f"Masukkan jumlah baru untuk {item[1]} (angka, 0 untuk hapus): ").strip()
                if not new.isdigit():
                    print("Input tidak valid. Masukkan angka (misal: 2) atau 0 untuk hapus.")
                    continue
                new = int(new)
                if new == 0:
                    keranjang.remove(item)
                    return f"{item[1]} dihapus dari keranjang karena jumlah diset 0."
                item[3] = new
                return f"Jumlah {item[1]} diubah menjadi {new}."
    return "Kode barang tidak ditemukan."


def menu_keranjang(keranjang):
    while True:
        tampil_keranjang(keranjang)

        print("\n[1] Belanja lagi")
        print("[2] Kurangi Barang / hapus barang")
        print("[3] Checkout")

        pilih = input("Pilih menu: ").strip()

        if pilih == "1":
            item = input_kode_barang()
            jumlah = input_jumlah_barang(item[1])
            print(tambah_barang(keranjang, item, jumlah))

        elif pilih == "2":
            print(ubah_jumlah(keranjang))

        elif pilih == "3":
            print("\nMelanjutkan ke checkout...")
            return keranjang

        else:
            print("Input tidak valid.")
