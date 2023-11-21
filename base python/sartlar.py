'''

LUNAPARK OYUN PROGRAMI
'''
YAS_SARTI = 12
YAS_SARTI_SON = 45
ZIYARETCI_YASI1 = 10
ZIYARETCI_YASI2 = 13

# BU ZİYARETÇİLERDEN HANGİSİ BİNEBİLİR


if ZIYARETCI_YASI1 < YAS_SARTI:  # 10<12  True (doğru)
    print("Buraya giremezsiniz 1")
elif ZIYARETCI_YASI1 > 45:
    print("Sen yaşlısın 1")
else:
    print("Giriş Serbest 1")

if ZIYARETCI_YASI2 < YAS_SARTI:  # 10<12  True (doğru)
    print("Buraya giremezsiniz 2")
elif ZIYARETCI_YASI2 > 45:
    print("Sen yaşlısın 2")


if ZIYARETCI_YASI1 < YAS_SARTI:  # 10<12  True (doğru)
    print("Buraya giremezsiniz")
else:
    print("Sen giriş yapabilirsin")

if ZIYARETCI_YASI2 < YAS_SARTI:  # 13 < 12 (yanlış)
    print("buraya giremezsiniz")
else:
    print("Sen giriş yapabilirsin")
