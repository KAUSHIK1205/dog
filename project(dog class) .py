class dog:
    species="german shepherd 🐕"
    def __init__(self,name,breed):
        self.name=name
        
        self.breed=breed

    def screen(self):
        print("\ndogs name:",self.name)
        print("\nspecies:",self.species)
        print("\nbreed🐕:",self.breed)





dog1=dog("lucifer"," alsatian wolf dog  ")

dog2=dog("deku"," king shepherd  ")

dog1.screen()

dog2.screen()

