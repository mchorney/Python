class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def display_health(self):
        print "The {}'s health is {}".format(self.name, self.health)


animal1 = Animal('Cat', 100)
animal1.walk().walk().walk().run().run().display_health()


class Dog(Animal):
    def __init__(self):
        self.name = 'Dog'
        self.health = 150

    def pet(self):
        self.health += 5
        return self


Dog().walk().walk().walk().run().run().pet().display_health()


class Dragon(Animal):
    def __init__(self):
        self.name = 'Dragon'
        self.health = 170

    def fly(self):
        self.health -= 10
        return self

    def display_health(self):
        super(Dragon, self).display_health()
        print 'I am a Dragon!'


Dragon().display_health()

animal2 = Animal('Giraffe', 120)
animal2.display_health()
