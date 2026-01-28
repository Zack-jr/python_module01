class Plant():
    def __init__(self, plant_name, plant_height, plant_age):
        self.plant_name = plant_name
        self.plant_height = plant_height
        self.plant_age = plant_age
class Flower(Plant):
    def __init__(self, plant_name, plant_height, plant_age, color_attribute):
        super().__init__(plant_name, plant_height, plant_age)
        self.color_attribute = color_attribute
    def bloom(self):
        print(f"{self.plant_name} is blooming beautifully!\n")

class Tree(Plant):
    def __init__(self, plant_name, plant_height, plant_age, trunk_diameter):
        super().__init__(plant_name, plant_height, plant_age)
        self.trunk_diameter = trunk_diameter
    def produce_shade(self):
        radius = (self.trunk_diameter / 100) / 2
        shade = (3.14 * (radius ** 2))
        print(f"{self.plant_name} provides {shade} square meters of shade\n")

class Vegetable(Plant):
    def __init__(self, plant_name, plant_height, plant_age, harvest_season, nutritional_value):
        super().__init__(plant_name, plant_height, plant_age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

flower_1 = Flower("Rose", 25, 30, "red")
flower_2 = Flower("Violet", 18, 30, "blue")

tree_1 = Tree("Oak", 500, 1825, 50)
tree_2 = Tree("Christmas tree", 200, 2, 8)

vegetable1 = Vegetable("Tomato", 80, 90, "summer harvest", "rich in vitamin C")
vegetable2 = Vegetable("Zucchini", 20, 32, "autumn harvest", "rich in antioxidants")

print("=== Garden Plant Types ===\n")
print(f"{flower_1.plant_name} ({type(flower_1).__name__}): {flower_1.plant_height}cm, {flower_1.plant_age} days, {flower_1.color_attribute} color")
flower_1.bloom()
print(f"{flower_2.plant_name} ({type(flower_2).__name__}): {flower_2.plant_height}cm, {flower_2.plant_age} days, {flower_2.color_attribute} color")
flower_2.bloom()
print(f"{tree_1.plant_name} ({type(tree_1).__name__}): {tree_1.plant_height}cm, {tree_1.plant_age} days, {tree_1.trunk_diameter}cm diameter")
tree_1.produce_shade()
print(f"{tree_2.plant_name} ({type(tree_2).__name__}): {tree_2.plant_height}cm, {tree_2.plant_age} days, {tree_2.trunk_diameter}cm diameter")
tree_2.produce_shade()
print(f"{vegetable1.plant_name} ({type(vegetable1).__name__}): {vegetable1.plant_height}cm, {vegetable1.plant_age} days, {vegetable1.harvest_season}")
print(f"{vegetable1.plant_name} is {vegetable1.nutritional_value}\n")
print(f"{vegetable2.plant_name} ({type(vegetable2).__name__}): {vegetable2.plant_height}cm, {vegetable2.plant_age} days, {vegetable2.harvest_season}")
print(f"{vegetable2.plant_name} is {vegetable2.nutritional_value}\n")

# Inheritance is when a "child object" uses the same attributes as the "parent object"
# We use super() to initialize directly the parent objects to reduce code lines
# We access the name of the object's class with type. Since everything is an object in python,
# we use .__name__ to access the actual string (the name)