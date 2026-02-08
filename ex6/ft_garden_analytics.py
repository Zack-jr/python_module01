class Plant:
    """initialize base plant attributes"""
    def __init__(self, plant_name, plant_age, plant_height):
        """Initialize plant with name, age, and height."""
        self.plant_name = plant_name
        self.plant_age = plant_age
        self.plant_height = plant_height

    def grow(self):
        """Increase plant height by 1cm and return a string"""
        self.plant_height += 1
        return f"{self.plant_name} grew 1cm"

    def __str__(self):
        """Return basic string representation of the plant."""
        return f"{self.plant_name}: {self.plant_height}cm"


class FloweringPlant(Plant):
    """Class for flowers"""
    def __init__(self, plant_name, plant_age, plant_height, color):
        """Initialize flowering plant with additional color attribute."""
        super().__init__(plant_name, plant_age, plant_height)
        self.color = color

    def __str__(self):
        """Return string"""
        return f"{super().__str__()}, {self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    """Flowers with prizes"""
    def __init__(self, plant_name, plant_age, plant_height, color, points):
        """Initialize prize flower with competitive points."""
        super().__init__(plant_name, plant_age, plant_height, color)
        self.prize_points = points

    def __str__(self):
        """Return string"""
        return f"{super().__str__()}, Prize points: {self.prize_points}"


class GardenManager:
    """Class used to create managers and manage multiple gardens"""
    total_managers = 0

    def __init__(self, name):
        """Initialize Garden"""
        self.manager_name = name
        self.plants = []
        self.total_growth = 0
        GardenManager.total_managers += 1

    class GardenStats:
        """calculating garden data analytics."""
        @staticmethod
        def calculate_score(plants):
            """Calculate total score based on height and prize points."""
            score = sum(p.plant_height for p in plants)
            score += sum(getattr(p, 'prize_points', 0) for p in plants)
            return score

        @staticmethod
        def get_type_counts(plants):
            """Return the count of plants by their specific class type."""
            reg = sum(1 for p in plants if type(p) is Plant)
            flow = sum(1 for p in plants if type(p) is FloweringPlant)
            prize = sum(1 for p in plants if type(p) is PrizeFlower)
            return reg, flow, prize

    def add_plant(self, plant):
        """Add a plant object to the current manager's garden."""
        print(f"Added {plant.plant_name} to {self.manager_name}'s garden")
        self.plants.append(plant)

    def grow_all(self):
        """Use the growth method for every plant in the garden."""
        print(f"{self.manager_name} is helping all plants grow...")
        for plant in self.plants:
            print(plant.grow())
            self.total_growth += 1

    @classmethod
    def create_garden_network(cls):
        """Class method to bootstrap a default network of managers."""
        return [cls("Alice"), cls("Bob")]

    @staticmethod
    def validate_height(plants):
        """Utility function to verify all plants have positive height."""
        if not plants:
            return False
        return all(p.plant_height > 0 for p in plants)


def main():
    print("=== Garden Management System Demo ===\n")
    m1, m2 = GardenManager.create_garden_network()

    m1.add_plant(Plant("Oak Tree", 25, 100))
    m1.add_plant(FloweringPlant("Rose", 2, 25, "red"))
    m1.add_plant(PrizeFlower("Sunflower", 1, 50, "yellow", 40))

    m2.add_plant(Plant("kaki tree", 5, 92))

    m1.grow_all()

    print(f"\n=== {m1.manager_name}'s Garden Report ===")
    print("Plants in garden:")
    for p in m1.plants:
        print(f"- {p}")

    stats = GardenManager.GardenStats
    reg, flow, prize = stats.get_type_counts(m1.plants)

    print(f"\nPlants added: {len(m1.plants)}, "
          f"Total growth: {m1.total_growth}cm")
    print(f"Plant types: {reg} regular, {flow} flowering, "
          f"{prize} prize flowers")
    print("\nHeight validation test: "
          f"{GardenManager.validate_height(m1.plants)}")

    score_a = stats.calculate_score(m1.plants)
    score_b = stats.calculate_score(m2.plants)
    print(f"Garden scores - Alice: {score_a}, Bob: {score_b}")
    print(f"Total gardens managed: {GardenManager.total_managers}")


if __name__ == "__main__":
    main()

# staticmethod: normal function that happens to be in a class,
# does not interact with the attributes
# classmethod: function in a class that uses or changes the data inside
# of the attributes.
# creating alice and bob as garden managers
