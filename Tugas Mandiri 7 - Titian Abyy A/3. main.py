import interest
import display

print("=== Program Kalkulator Bunga Tabungan Nobita ===")
principal = float(input("Masukkan saldo awal Nobita:"))
rate = float(input("Masukkan bunga tahunan Nobita:"))
years = int(input("Masukkan lama menabung Nobita:"))

ci = interest.compound_interest(principal, rate, years)
si = interest.simple_interest(principal, rate, years)

display.print_result(principal, rate, years, ci, si)