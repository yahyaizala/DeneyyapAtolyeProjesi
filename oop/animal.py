class Animal:

    def __init__(self):
        self.name = "Tanımsız"
        self.yas = 0
        self.sahip = None

    def set_name(self, name):
        self.name = name

    def set_yas(self, yas):
        self.yas = yas

    def set_sahip(self, sahip):
        self.sahip = sahip

    def __str__(self):
        print(f"adı : {self.name} sahibi : {self.sahip} , yaş :{self.yas} ")
