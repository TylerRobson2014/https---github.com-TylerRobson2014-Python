import math
import random

class Sith(object):

    def __init__(self,name):

        self.name = name
        self.armor = 100
        self.life = 100
        self.speed = 5
        self.strength = 100
        self.position = 0
        self.alive = True

    def whois(self):
        return self.name

    def location(self):
        return self.position


    def choice(self,enemy):

        enemyposition = enemy.location()

        if math.fabs(enemyposition - self.position)< 5:
            self.slash_light_saber(enemy)
        elif math.fabs(enemyposition - self.position)> 100:
            self.force(enemy)
        else:
            self.move()

    def force(self,enemy):
        enemy.move(-(math.fabs(enemy.location() - self.position))/4)
        self.strength -= 0.1*((math.fabs(enemy.location() - self.position))/4)

    def is_alive(self):

        if self.alive:
            return True
        else:
            return False
        

    def slash_light_saber(self,enemy):

        #print (self.name, "slashes",enemy.whois(), "with lightsaber")

        enemy.hit(enemy)

    def dodge(self):

        # print (self.name, "dodged the blast")
        return False

    def block(self):

        #print (self.name, "blocked the blast")
        return False

    def hit(self,enemy):

        randomchoice = random.randint(1,6)

        if randomchoice > 4:
            self.dodge()
        elif randomchoice == 3:
            self.block()
        else:
            self.armor -= 20
            if self.armor > 0:
                self.strength -=5
                self.speed = self.speed*0.95
           #     print (self.name, "has been hit but armor held",self.strength)
            else:
                self.strength -=40
                self.speed = self.speed*0.70
            #    print(self.name, "has been hit and armor breached",self.strength)
            if self.strength < 0:
                self.die()

    def die(self):

        #print(self.name, "dies")
        self.alive = False

    def move(self):

        #print (self.name, "moves forward")
        self.position += 2*self.speed




class Storm_Trooper(object):

    def __init__(self,name):

        self.name = name
        self.armor = 300
        self.life = 100
        self.speed = 5
        self.strength = 100
        self.position = random.randint(50,200)
        self.alive = True

    def whois(self):
        return self.name


    def choice(self,enemy):

        enemyposition = enemy.location()

        if math.fabs(enemyposition - self.position)> 20:
            self.fire_blaster(enemy)
        else:
            self.move(self.speed)

    def location(self):
        return self.position


    def is_alive(self):
        if self.alive:
            return True
        else:
            return False

    def fire_blaster(self,enemy):

        #print (self.name, "blasts opponent with laser baster")

        enemy.hit(enemy)

    def hit(self, enemy):

        enemyposition = enemy.location()

        if math.fabs(enemyposition - self.position)< 5:

            self.armor -= 20
            if self.armor > 0:
                self.strength -=5
                self.speed = self.speed*0.95
         #       print(self.name, "has been hit but armor held",self.strength)
            else:
                self.strength -=40
                self.speed = self.speed*0.7
          #      print(self.name, "has been hit and armor breached",self.strength)
            if self.strength < 0:
                self.die()

    def move(self,step):

        #print (self.name, "moves back")
        self.position += step

    def die(self):

        #print(self.name, "dies")
        self.alive = False


random.seed()

sith_win = 0
trooper_win = 0

end = int(input("Enter the number of trials: "))

for i in range(1,end):

    sith = Sith("Fred")
    trooper = Storm_Trooper("Bob")


    while (sith.is_alive() and trooper.is_alive()):
        trooper.choice(sith)
        sith.choice(trooper)
            

    if sith.is_alive():
        sith_win += 1
    else:
        trooper_win += 1

print ("sith wins", sith_win, "trooper wins", trooper_win)
    












