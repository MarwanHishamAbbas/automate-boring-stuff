class Bike:
    def __init__(self, color, material):
        self.color = color
        self.material = material

    def brake(self):
        print("Braking!...")
   

    



red_bike = Bike('red', 'metal')
blue_bike = Bike('blue', 'Steel')
red_bike.brake()

print(id(red_bike))
print(id(blue_bike))
        