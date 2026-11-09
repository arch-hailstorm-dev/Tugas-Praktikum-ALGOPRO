def print_result(principal, rate, years, ci, si):
    """Menampilkan Hasil Perhitungan Bunga Tabungan Nobita"""
    print("\n==== Hasil Perhitungan Tabungan ====")
    print(f"Saldo Awal                     : {principal:,.1f}")
    print(f"Bunga Tahunan                  : {rate * 100:.1f}")
    print(f"Lama Menabung                  : {years} tahun")
    
    print("-"*60)  
    
    print(f"Nilai Akhir (Bunga Majemuk)    : {ci:.2f}")
    print(f"Nilai Akhir (Bunga Sederhana)  : {si:,.2f}")
    
    print('='*60)
    