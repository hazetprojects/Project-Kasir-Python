from input_barang import input_kode_barang, input_jumlah_barang
from menu_keranjang import menu_keranjang

def keranjang_belanja():
    keranjang = []

    print("\n==== Keranjang Belanja ===")

    while True:
        try:
            berapa_kali = int(input("Berapa jenis barang yang ingin anda beli ? "))
            if berapa_kali >= 1:
                break
            print("Minimal pembelian 1 barang")
        except ValueError:
            print("Masukkan angka yang valid !")

    for i in range(berapa_kali):
        print(f"\nBarang ke - {i+1}:")
        item = input_kode_barang()
        jumlah = input_jumlah_barang(item[1])
        keranjang.append([item[0], item[1], item[2], jumlah])


    keranjang = menu_keranjang(keranjang)
    return keranjang
