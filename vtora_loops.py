#Da se napravi programa vo koja korisnikot ke kaze kolku pati da se povtoruva ciklusot, 
# da vnese suma vo denari i da se napravi konverzija vo evra

pati=int(input("Vnesete kolku pati ke se povtoruva cikulusot"))
for i in range(pati):
    suma=int(input("Vnesete go iznosot shto treba da se konvertira vo evraa"))
    nova_suma=suma*61.69
    print("Sumata konvertirana vo evra spored sreden kurs na NRBM iznesuva: {} EUR".format(nova_suma))