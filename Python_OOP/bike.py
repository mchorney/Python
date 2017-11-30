class Bike(object):

    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def ride(self):
        print "RIDING,"
        self.miles += 10
        return self

    def reverse(self):
        print "REVERSING,"
        self.miles -= 5
        return self

    def displayinfo(self):
        print "Your bike cost $", str(self.price), "its maximum speed is", str(self.max_speed), "and it has", str(self.miles), "miles on it."
        return self


newbike = Bike(20, 35)
newbike.ride().ride().displayinfo()

crappybackwardsbike = Bike(10, 40)
crappybackwardsbike.reverse().reverse().displayinfo()
