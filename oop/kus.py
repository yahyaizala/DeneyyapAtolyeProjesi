from animal import Animal


class Kus(Animal):
    def uc(self):
        print(f"Ben uçuyorum detaylar")
        self.__str__()

    def __init__(self, name):
        # super().__init__() bu yöntem de sorunsuz çalışır.
        super(Kus, self).__init__()
        self.name = name
        print(f"isim verildi {self.name}")


karga = Kus(name="Karga")
karga.uc()
