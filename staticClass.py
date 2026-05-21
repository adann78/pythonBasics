class Person:
    species="Humano"

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def change_species(self,new_species):
        self.species=new_species
person1 = Person("Adan", 47)
person2=Person("Alexandra", 20)
print(person1.species)
print(person2.species)
person1.change_species("Alien")
print(person1.species)
