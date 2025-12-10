from hitung import hitung_total

def tampilkan_struk(keranjang, nama_user="", bayar=0, kembalian=0):
    subtotal_perbarang, total_sebelum_diskon, diskon, total_setelah_diskon, persen_diskon = hitung_total(keranjang)

    total_sebelum_diskon = int(total_sebelum_diskon)
    diskon = int(diskon)
    total_setelah_diskon = int(total_setelah_diskon)

    print("\n===== STRUK BELANJAAN =====")
    if nama_user:
        print(f"\nNama Pembeli: {nama_user}\n")

    print(f"{'Barang':<30} {'Harga':>10} {'Jumlah':>8} {'Subtotal':>15}")
    print("-" * 72)

    for i, item in enumerate(keranjang):
        nama = item[1]
        harga = int(item[2])
        jumlah = int(item[3])
        subtotal = int(subtotal_perbarang[i])

        harga_str = f"Rp {harga:,}"
        subtotal_str = f"Rp {subtotal:,}"

        print(f"{nama:<30} {harga_str:>10} {jumlah:>8} {subtotal_str:>15}")

    print("-" * 72)
    print(f"{'Total sebelum diskon':<30} : Rp {int(total_sebelum_diskon):,}")
    print(f"Diskon ({persen_diskon}%)".ljust(30) + f" : Rp {int(diskon):,}")
    print(f"{'Total setelah diskon':<30} : Rp {int(total_setelah_diskon):,}")
    print(f"{'Uang dibayar':<30} : Rp {int(bayar):,}")
    print(f"{'Kembalian':<30} : Rp {int(kembalian):,}")
    print("-" * 72)
    print("\nTerima kasih telah berbelanja di SMART SCHOOL SUPPLIES STORE")
