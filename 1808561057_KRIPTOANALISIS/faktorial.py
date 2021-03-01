# IGA MIRAH AGUNG JAYANTI (1808561057) / KRIPTOANALISIS
# PROGRAM UNTUK MENCARI BILANGAN FAKTORIAL

#Program mencari nilai faktorial
def faktorial(x):
    hasil = 1
    for i in range(2, x + 1):
        hasil *= i
    return hasil

n = int(input("Masukkan bilangan: "))
print("Nilai Faktorial dari", n, "= ", faktorial(n))