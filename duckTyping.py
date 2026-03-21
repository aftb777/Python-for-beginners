# Duck Typing = concept where the class of an object is less important than the methods 
#               class type is not checked if minimum methods/attributes are present
#               "If it walks like a duck and quack like a duck then it must be duck"

class Duck():
    
    def walk(self):
        print("This duck is walking")
        
    def talk(self):
        print("this duck is quacking")
        
class Chiken:
    
    def walk(self):
        print("this chicken is walking")
        
    def talk(self):
        print("This chicken is clucking")
        
class Person():
    
    def catch(self , duck):
        duck.walk()
        duck.talk()
        print("You caught the critter !")
        
duck = Duck()
chiken = Chiken()
person = Person()

person.catch(chiken)
print()
person.catch(duck)