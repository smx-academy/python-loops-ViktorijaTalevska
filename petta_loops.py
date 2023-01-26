#Da se napravi programa za potrebite na nekoja prodavnica. Korisnikot da moze vnesuva produkti i
#  cenite se dodeka ne izbere deka poveke ne saka da vnesuva. Koga ke prestane da vnesuva produkti
#  da se ispecati kolku vkupno ima za plakjanje, da plati i da se presmeta dali i kolku treba
#  da se vrati kusur.
print("Vnesuvajte produkti se dodeka ne napishete stop")
br=0
while  True:
    produkt=input("Vnesi ime na produkt")
    cena=int(input("Vnesi cena na produkt"))
    vkupno=+cena
if produkt=="stop":
break
print("Imate {} denari za plakanje.Ve molime vnesete ja kesh sumata koja ja poseduvate".format(vkupno))
kesh=int(input())
kusur=kesh-vkupno
if kesh-vkupno!=0:
    print("Imate {} denari kusur.Ve molime podignete go".format(kesh-vkupno))
elif kesh-vkupno==0:
    print("Vi blagodarime")
else:
    print("Greshka vo vnesuvanjeto")


