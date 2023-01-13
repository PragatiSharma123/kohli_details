class SuperHeroes():
   def __init__(self, name, superpower):
        self.name = name
        self .superpower = superpower


   def get_superpower(self): 
     print(f"\nI am {self.name} and my power is {self.superpower}")

Super_heroes = SuperHeroes(name="Ironman",superpower="suit")
Super_heroes.get_superpower()

ironMan = SuperHeroes(name="Ironman", superpower="suit")
print(ironMan.name)
print(ironMan.superpower)
    
ironMan.get_superpower()

thor = SuperHeroes(name="Thor",superpower="suit")
print(thor.name)
print(thor.superpower)
thor.get_superpower()

    
