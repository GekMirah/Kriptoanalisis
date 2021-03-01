# IGA MIRAH AGUNG JAYANTI (1808561057) / KRIPTOANALISIS
# PROGRAM UNTUK MENCARI BILANGAN PRIMA

faktor = 0
bilangan = int(input('masukkan bilangan : '))
a = 1
while(a<=bilangan):
    if(bilangan%a==0):
        faktor=faktor+1
    a=a+1
if(faktor == 2):
    print('Bilangan Prima')
else:
    print('bukan bilangan prima')