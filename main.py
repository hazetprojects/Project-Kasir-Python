from persediaan import barang_list
from tampilan import header_toko, login_user, tampilkan_barang
from keranjang import keranjang_belanja
from hitung import hitung_total
from pembayaran import pembayaran_cash
from struk import tampilkan_struk

def main():
    header_toko()
    nama_user = login_user()
    tampilkan_barang()

    keranjang = keranjang_belanja()

    subtotal_perbarang, total_sebelum_diskon, diskon, total_setelah_diskon, persen_diskon = hitung_total(keranjang)


    bayar, kembalian = pembayaran_cash(total_setelah_diskon)

    tampilkan_struk(keranjang, nama_user, bayar=bayar, kembalian=kembalian)

if __name__ == "__main__":
    main()
