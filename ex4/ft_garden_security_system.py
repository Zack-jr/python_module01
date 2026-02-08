class SecurePlant():
    """Safe Plant class"""

    """Initialize secure plant's attributes"""
    def __init__(self, plant_name, plant_height, plant_age):
        self.plant_name = plant_name
        self._plant_height = plant_height
        self._plant_age = plant_age

    """Setter method to change height safely"""
    def set_height(self, new_height):
        if new_height > 0:
            self._plant_height = new_height
            print(f'Height updated: {new_height}cm [OK]')
        else:
            print(f"\nInvalid operation attempted: "
                  f"height {new_height} [REJECTED]")
            print("Security: Negative height rejected\n")

    """Setter method to change the plant's age safely"""
    def set_age(self, new_age):
        if new_age > 0:
            self._plant_age = new_age
            print(f'Age updated: {new_age} days [OK]\n')
        else:
            print(f"\nInvalid operation attempted: age {new_age} [REJECTED]")
            print("Security: Negative age rejected\n")

    """Getter function to get the plants' height safely"""
    def get_height(self):
        return self._plant_height

    """Getter function to get the plant's age safely"""
    def get_age(self):
        return self._plant_age


print("=== Garden Security System ===")
plant1 = SecurePlant("Rose", 25, 30)
print(f"Plant created: {plant1.plant_name}")
plant1.set_height(-121)
plant1.set_age(12)

print(f"Current plant: {plant1.plant_name} ({plant1.get_height()}cm, "
      f"{plant1.get_age()} days)")

# hiding the object's attributes with an underscore to add a small protection
# adding conditons to the methods to make sure the value
# is not getting corrupted
