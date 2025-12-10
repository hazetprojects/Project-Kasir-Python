from persediaan import barang_list

def header_toko():

    print("\n===================================")
    print("=== SMART SCHOOL SUPPLIES STORE ===")
    print("===================================\n")

def login_user():
    print("Silahkan login dahulu")
    
    nama_user = input("Masukkan nama anda : ").strip()
    print(f"\nSelamat datang {nama_user}, ingin membeli apa ?\n")
    return nama_user

def tampilkan_barang():
    print("==== DAFTAR BARANG ====\n")
    print(f"{'Kode':<6} {'Barang':<25} {'Harga':>6}")
    print("-" * 52)

    for kode, barang, harga in barang_list:
        print(f"{kode:<6} {barang:<25} Rp {harga:>7,}")

    print("-" * 52)
    