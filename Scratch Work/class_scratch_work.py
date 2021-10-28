class Cat:
    population = 0

    def __init__(self, name):
        self.name = name
        Cat.population += 1

def main():
    cat1 = Cat("Pat")
    cat2 = Cat("Pepper")
    cat3 = Cat("Pouncy")

    Cat.population = 4
    cat3.population = 5
    print("The cat population is:", Cat.population)
    print("The cat population is:", cat2.population)
    print("The cat population is:", cat1.population)
    print("The cat population is:", cat3.population)


main()