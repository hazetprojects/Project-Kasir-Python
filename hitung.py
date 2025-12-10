def hitung_total(keranjang):

    subtotal_perbarang = []
    total_sebelum_diskon = 0

    for item in keranjang:
        subtotal = item[2] * item[3]
        subtotal_perbarang.append(subtotal)
        total_sebelum_diskon += subtotal

    if total_sebelum_diskon >= 100000:
        persen_diskon = "10"
        diskon = 0.10 * total_sebelum_diskon

    elif total_sebelum_diskon >= 50000:
        persen_diskon = "5"
        diskon = 0.05 * total_sebelum_diskon
    
    else:
        persen_diskon = "0"
        diskon = 0

    total_setelah_diskon = total_sebelum_diskon - diskon

    return subtotal_perbarang, total_sebelum_diskon, diskon, total_setelah_diskon, persen_diskon