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
#birds = mammal("Bird","Reptile",is_warm_blooded=True)
#birds.idennity()



class Bird(Aminal):
    def __init__(self,name,specis,can_fly=True):
        super().__init__(name,specis)
        self.can_fly = can_fly
    def fly(self):
        if self.can_fly:
            print(f"{self.name} is flying.")
        else:
            print(f"{self.name} is not flying.")
    def speak(self):
        print(f"{self.name} of {self.specis} speaks.")




class Zookeeper():
    def __init__(self,name):
        self.name = name
    def feed(self,animal):
        print(f"{self.name} is feeding.{animal.name}.")
    def put_to_sleep(self,animal):
        print(f"{self.name} put to{animal.name} sleep.")
    def move_animal(self,animal):
        print(f"{self.name} moved {animal.name}.")
snake=mammal("Snake","Reptail",is_warm_blooded=True)
parrot=Bird("Parrot","Reptail",can_fly=True)
fox=mammal("Fox","Reptail",is_warm_blooded=False)
zookeeper=Zookeeper("Rahim")
zookeeper.feed(fox)
zookeeper.put_to_sleep(parrot)
zookeeper.move_animal(snake)



fox.speak()
snake.rest()
parrot.fly()
fox.warm_blooded()