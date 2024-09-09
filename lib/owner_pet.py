class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all =[]

    def __init__(self,name,pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise ValueError("Invalid pet typr")

        if not isinstance(name, str):
            raise ValueError("Name must be a string")

        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)
        

class Owner:
    def __init__(self,name):
        self.name = name
        self._pets = []

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
        

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Pet must be an instance of Pet")
        if pet.owner:
            pet.owner._pets.remove(pet)
        pet.owner = self  
        self._pets.append(pet)


    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
  