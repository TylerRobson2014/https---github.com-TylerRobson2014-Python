import math
import random

class Sith(object):

    def __init__(self,name):

        self.name = name
        self.armor = 100
        self.life = 100
        self.speed = 100
        self.strength = 100
        self.position = 0
        self.alive = True

    def slash_light_saber(self,enemy):

        print (self.name, "slashes opponent with lightsaber")

        enemy.hit()

    def dodge(self):

        print (self.name, "dodged the blast")

    def block(self):

        print (self.name, "blocked the blast")

    def hit(self):

        self.armor -= 20
        self.strength -=10
        print(self,name, "has been hit")
        if self.strength < 0:
            self.die()

    def die(self):

        print(self,name, "dies")
        self.alive = False

    def move(self):

        print (self.name, "moves forward")
        self.position += 20




class Storm_Trooper(object):

    def __init__(self,name):

        self.name = name
        self.armor = 200
        self.life = 100
        self.speed = 80
        self.strength = 100
        self.position = 100
        self.alive = True

    def fire_blaster(self,enemy):

        print (self.name, "blasts opponent with laser baster")

        enemy.hit()
        print(self,name, "hit")

    def hit(self):

        self.armor -= 20
        print(self,name, "has been hit")
        self.strength -=10
        print(self,name, "has been hit")
        if self.strength < 0:
            self.die()


    def move(self):

        print (self.name, "moves back")
        self.position -= 10

    def die(self):

        print(self,name, "dies")
        self.alive = False


sith = Sith("Fred")

trooper = Storm_Trooper("Bob")

sith.slash_light_saber(trooper)







