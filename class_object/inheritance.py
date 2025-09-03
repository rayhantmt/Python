class Aminal:
    def __init__(self,name,specis):
        self.name = name
        self.specis = specis
    def idennity(self):
        print(f"{self.name} is from  {self.specis} specis.")
    def eat(self):
        print(f"{self.name} is eating.")
    def sleep(self):
        print(f"{self.name} is sleeping.")
    def rest(self):
        print(f"{self.name} is resting.")
class mammal(Aminal):
    def __init__(self,name,specis,is_warm_blooded=True):
        super().__init__(name,specis)
        self.is_warm_blooded = is_warm_blooded
    def warm_blooded(self):
        if self.is_warm_blooded:
            print(f"{self.name} is warm blooded.")
        else:
            print(f"{self.name} is not warm blooded.")
    def speak(self):
        print(f"{self.name} of {self.specis} speaks.")
birds = mammal("Bird","Reptile",is_warm_blooded=True)
birds.idennity()


