class plant():
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


first = plant('Rose', 25, 30)
second = plant('Sunflower', 80, 45)
third = plant('Cactus', 15, 120)

print('=== Garden Plant Registery ===')
print(f'{first.name}: {first.height}cm, {first.age} days old')
print(f'{second.name}: {second.height}cm, {second.age} days old')
print(f'{third.name}: {third.height}cm, {third.age} days old')

# almost like structs but need to define with class and
# use __init__ to create the variables
# use a "self" variable in the definition to store the data
# and assign values
# access values like structs in C
