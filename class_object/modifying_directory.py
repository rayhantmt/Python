class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def displayinfo(self):
        self.brand="BMW"
        print(f"Car brand: {self.brand} and model: {self.model}")
obj=car("Mercedez","Benz")
obj.brand="Ford"
obj.model="Mustang"
obj.displayinfo()
print(obj.brand)
print(obj.model)
print(obj.displayinfo())
obj.brand="BMW"
obj.model="Mercedez"
obj.displayinfo()