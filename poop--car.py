from poop import Car

car_1 = Car("Chevy", "Corvette", 2021, "Blue")
car_2 = Car("Ford","Mustang",2022,"Red")

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)

print(car_2.color)
print(car_2.model)


car_2.drive()
car_1.stop()
