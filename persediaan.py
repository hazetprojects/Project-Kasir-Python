barang_list = [
    ["AT01", "Pensil", 2000],
    ["AT02", "Pulpen", 2500],
    ["AT03", "Penghapus", 1500],
    ["AT04", "Penggaris Plastik", 5000],
    ["AT05", "Penggaris Besi", 9000],
    ["AT06", "Buku Tulis", 12000],
    ["AT07", "Buku Gambar", 15000],
    ["AT08", "Sampul Buku Coklat", 2000],
    ["AT09", "Sampul Buku Bening", 2000],
    ["AT10", "Tipe-x Cair", 5000],
    ["AT11", "Gunting", 6000],
    ["AT12", "Cutter", 7000],
    ["AT13", "Lem Kertas", 5000],
    ["AT14", "Spidol Warna/lusin", 15000],
    ["AT15", "Spidol Whiteboard", 5000]
]

def cari_barang(kode):
    kode = kode.upper()
    for item in barang_list:
        if item[0] == kode:
            return item
    return None

