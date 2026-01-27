class SecurePlant():
    def __init__(self, plant_name, plant_height, plant_age):
        self.plant_name = plant_name
        self._plant_height = plant_height
        self._plant_age = plant_age
    
    def set_height(self, new_height):
        if new_height > 0:
            self._plant_height = new_height
            print(f'Height updated: {new_height}cm [OK]')
        else:
            print(f"\nInvalid operation attempted: height {new_height} [REJECTED]")
            print("Security: Negative height rejected\n")

    def set_age(self, new_age):
        if new_age > 0:
            self._plant_age = new_age
            print(f'Age updated: {new_age} days [OK]\n')
        else:
            print(f"\nInvalid operation attempted: age {new_age} [REJECTED]")
            print("Security: Negative age rejected\n")

    def get_height(self):
        return self._plant_height

    def get_age(self):
        return self._plant_age

print("=== Garden Security System ===")
plant1 = SecurePlant("Rose", 25, 30)
print(f"Plant created: {plant1.plant_name}")
plant1.set_height(-121)
plant1.set_age(12)

print(f'Current plant: {plant1.plant_name} ({plant1.get_height()}cm, {plant1.get_age()} days)')

# initializing the object and his attributes with an underscore to hide the object's attributes
# not initializing plant_name as _plant_name since we don't have a get_name method here so it's pointless
# to hide the name
# adding conditons to the methods to make sure the value is not getting corrupted