from random import randint

class Animal:
    def __init__(self, age, type):
        self.age = age
        self.type = type
        self.next = None
        

class Queue:
    def __init__(self, list_of_animals = []):
        if len(list_of_animals) == 0:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            self.head = list_of_animals[0]
            self.tail = self.head
            self.length = 1

            if len(list_of_animals) > 1:
                index = 1
                while index < len(list_of_animals):
                    self.enqueue(list_of_animals[index])
                    index += 1


    def enqueue(self, animal):
        if (self.head == None) and (self.tail == None):
            self.head = self.tail = animal
        else:
            self.tail.next = animal
            self.tail = self.tail.next

        self.length += 1


    def dequeue(self):
        if (self.head == None) and (self.tail == None):
            raise Exception("There are no animals left.")
        else:
            animal = self.head
            self.head = self.head.next
            animal.next = None
            self.length -= 1
            return animal
        

class QueuesOfAnimals:
    def __init__(self, list_of_dogs = [], list_of_cats = []):
        self.dogs = Queue(list_of_dogs)
        self.cats = Queue(list_of_cats)

    
    def enqueue(self, animal):
        if animal.type == "cat":
            self.cats.enqueue(animal)
        elif animal.type == "dog":
            self.dogs.enqueue(animal)
        else:
            raise Exception("Can't Enqueue anything that isn't a cat or a dog.")

    
    def dequeueDog(self):
        if self.dogs.length > 0:
            return self.dogs.dequeue()
        else:
            raise Exception("There are no dogs left.")


    def dequeueCat(self):
        if self.cats.length > 0:
            return self.cats.dequeue()
        else:
            raise Exception("There are no cats left.")


    def dequeueAny(self):
        if (self.cats.length > 0) and (self.dogs.length > 0):
            if randint(0, 1):
                return self.dequeueCat()
            else:
                return self.dequeueDog()
        elif self.cats.length > 0:
            return self.dequeueCat()
        elif self.dogs.length > 0:
            return self.dequeueDog()
        else:
            raise Exception("There aren't any animals left")


if __name__ == "__main__":
    all_animals = QueuesOfAnimals([Animal(7, "dog"), Animal(6, "dog"), Animal(5, "dog")],
                                  [Animal(3, "cat"), Animal(2, "cat"), Animal(1, "cat")])

    print(all_animals.dequeueAny().age)
    print(all_animals.dequeueAny().age)
    print(all_animals.dequeueAny().age)
    print(all_animals.dequeueAny().age)
    print(all_animals.dequeueAny().age)
    print(all_animals.dequeueAny().age)
