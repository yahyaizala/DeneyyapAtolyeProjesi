ad = "Yahya"
soyad = "İzala"

# ikisini birleştirelim
ad_soyad = ad + soyad  # hiç boşluk yok
print(ad_soyad)
ad_soyad = ad + " " + soyad  # araya boşluk koyduk
print(ad_soyad)
ad_soyad = f"{ad} {soyad}"  # daha temiz -> Çok rahat çok profesyonel
print(ad_soyad)

metin = "Yahya İzala Kocaeli Üniversitesi"
# parçalara bölelim  (boşluklara göre)
print(metin.split())  # çıktısı -> ['Yahya', 'İzala', 'Kocaeli', 'Üniversitesi']

