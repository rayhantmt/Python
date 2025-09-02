class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def displayinfo(self):
        print(f"Car brand: {self.brand} and model: {self.model}")
obj=car("Mercedez","Benz")
obj.brand="Ford"
obj.model="Mustang"
obj.displayinfo()