class Pet: 
  def __init__ (self, name, age):
      self.name = name
      self.age = age
  def get_human_age(self):
      self.get_human_age = (self.age * 7)
      return self.get_human_age


class Spieces(Pet): # Inherit from Pet class
      def __init__ (self, name, age, spieces): # Add name and age parameters
        super().__init__(name, age) # Call the parent class constructor
        self.spieces = spieces  

      def get_spieces(self):
        return self.spieces

      def spieces_lifespan(self):
        if self.spieces == "dog":
          self.spieces_lifespan = 10
        elif self.spieces == "cat":
          self.spieces_lifespan = 15
        else:
          self.spieces_lifespan = 20
        return self.spieces_lifespan

pet1 = Spieces("trixie", 6, "dog") # Create instances of Spieces with name and age

pet2 = Spieces("fluffy", 4, "cat")

pet3 = Spieces("fido", 8, "goat")



# Call the spieces_lifespan method on each pet object
for pet in [pet1, pet2, pet3]:
  print("The pet name is ", pet.name, "and they are", str.strip(str(pet.age)), ".", "Their speices is a", pet.spieces, "and they are", pet.get_human_age(), "in human years.", "But their average spieces life span is", pet.spieces_lifespan(), "years")