class Car(object):

    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if (price > 10000):
            self.tax = 15
        else:
            self.tax = 12

    def display_all(self):

        print "Price:", self.price
        print "Speed:", self.speed, "mph"
        print "Fuel:", self.fuel
        print "Mileage:", self.mileage, "mpg"
        print "Tax:", self.tax


newcar = Car(20000, 50, "full", 40)
newcar.display_all()

fancynewcar = Car(120000, 50, "full", 40)
fancynewcar.display_all()

crappynewcar = Car(500, 5, "empty", 4)
crappynewcar.display_all()
