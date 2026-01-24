class Car():
    def __init__(self,model,year,color):
        self.model = model
        self.year = year
        self.color = color

    def max_speed(self):
        return len(self.model)*60
    
    def __str__(self):
        return f"{self.year} model {self.color} {self.model}."
    
    def __len__(self):
        return len(self.model)

Tesla = Car("Tesla",2024,"red")
Lambo = Car("Lamborghini", 2025, "black")

print(Tesla.max_speed())
print(Lambo.max_speed())
print(Tesla)
print(Lambo)