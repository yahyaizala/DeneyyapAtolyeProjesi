alinacak_listesi = ["Elma", "Domates", "Yumurta"]

print(alinacak_listesi)

for alinacak in alinacak_listesi:  # teker teker içinde dolaşıyoruz
    print(alinacak)

for i, alinacak in enumerate(alinacak_listesi):  # sıralı bir şekilde dolaşıyoruz.
    print(i, alinacak)  # i harfi index anlamına geliyor

# listeye eklem appand

alinacak_listesi.append("Havuç")
alinacak_listesi.append("Patates")
print(alinacak_listesi)  # ['Elma', 'Domates', 'Yumurta', 'Havuç', 'Patates']

# listeden silme işlemi remove

alinacak_listesi.remove("Elma")
print(alinacak_listesi)  # ['Domates', 'Yumurta', 'Havuç', 'Patates']

# bir değerin hangi sırada olduğunu bulmak --> index bulmak

i = alinacak_listesi.index("Patates")
# hata yakalama komutu try except
try:
    i_elma = alinacak_listesi.index("Elma")
    print(f"Patatesin index değeri {i_elma}")
except:
    print("Elma listede mevcut değildir.")
print(f"Patatesin index değeri {i}")
