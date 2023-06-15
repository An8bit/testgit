def tim_uoc_chung_lon_nhat(a, b):
    if a > b:
        lon, nho = a, b
    else:
        lon, nho = b, a
    while nho != 0:
        temp = nho
        nho = lon % nho
        lon = temp
    return print("manh nhat",lon)
    //ngu hahaha
tim_uoc_chung_lon_nhat(24,6)
