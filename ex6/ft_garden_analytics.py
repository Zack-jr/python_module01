class GardenManager():
    def __init__(self, manager_name):
            self.manager_name = manager_name

    @classmethod
    def create_garden_network(cls):
        manager1 = cls("Alice")
        manager2 = cls("Bob")
        return [manager1, manager2]
    @classmethod
    def add_plant()

   # class GardenStats():
    #    @staticmethod
     #   def analytics()


class Plant():
    def __init__(self, plant_name, plant_age, plant_height):
        self.plant_name = plant_name
        self.plant_age = plant_age
        self.plant_height = plant_height
    def grow(self):
        self.plant_height += 1
    def age(self):
        self.plant_age += 1

class FloweringPlant(Plant):
    def __init__(self, plant_name, plant_age, plant_height, color_attribute):
        super().__init__(plant_name, plant_age, plant_height)
        self.color_attribute = color_attribute

class PrizeFlower(FloweringPlant):
    def __init__(self, plant_name, plant_age, plant_height, color_attribute, prize_points):
        super().__init__(plant_name, plant_age, plant_height, color_attribute)
        self.prize_points = prize_points

def title(title_str):
    print(f"=== {title_str}===")

def main():
    title("Garden Management System Demo")
    manager1, manager2 = GardenManager.create_garden_network()
    print(f"{manager1.manager_name}, {manager2.manager_name}")


if __name__ == "__main__":
    main()

# creating Alice and Bob as garden managers

# staticmethod: normal function that happens to be in a class, does not interact with the attributes
# classmethod: function in a class that uses or changes the data inside of the attributes.