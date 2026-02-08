class plant():
    """Initialize plant's attributes"""
    def __init__(self, plant_name, plant_height, plant_age):
        self.plant_name = plant_name
        self.plant_height = plant_height
        self.plant_age = plant_age


plants_list = [
    ("Rose", 25, 30),
    ("Oak", 200, 365),
    ("Cactus", 5, 90),
    ("Sunflower", 80, 45),
    ("Fern", 15, 120)
]
count = 0
for i in plants_list:
    element = plant(*i)
    print(f"Created: {element.plant_name} ({element.plant_height}cm, "
          f"{element.plant_age} days)")
    count += 1
print(f'\nTotal plants created: {count}')

# a tuple is an ordered and fixed collection of elements
# using an list of tuples to initialize my plant plants all at once
# use * to initialize the tuple (has to be ordered)
