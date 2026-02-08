class plant():
    """Initialize the plant's attributes"""
    def __init__(self, plant_name, plant_height, plant_age):
        self.plant_name = plant_name
        self.plant_height = plant_height
        self.plant_age = plant_age

    """Method to grow the plant by 1"""
    def grow(self):
        self.plant_height += 1

    """Method to increase the plant's age by 1"""
    def age(self):
        self.plant_age += 1

    """Method to print the plant's info"""
    def get_info(self):
        print(f"{self.plant_name}: {self.plant_height}cm, "
              f"{self.plant_age} days old")


first = plant('Rose', 25, 30)
second = plant('Sunflower', 80, 45)
third = plant('Cactus', 15, 120)

i = 1
while i <= 7:
    print(f'=== Day {i} ===')
    first.get_info()
    second.get_info()
    third.get_info()
    first.grow()
    second.grow()
    third.grow()
    first.age()
    second.age()
    third.age()
    i += 1


print('Growth this week: +6cm')
# same as previous but adding new methods
# methods are basically functions within a class
# get the infos, grow and age the plants for each day of the week.
