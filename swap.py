print("Swap")
ageOne = 21
ageTwo = 16

print(ageOne,ageTwo)

def swapAge (ageOne, ageTwo):
    storAge = ageOne
    ageOne = ageTwo
    ageTwo = storAge
    return ageOne, ageTwo
  
age1,age2 = swapAge(ageOne, ageTwo)

print(age1,age2)
