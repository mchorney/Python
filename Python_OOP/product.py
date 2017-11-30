class Product(object):
    def __init__(self, price, name, weight, brand, cost):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = 'For Sale'

    def sell(self):
        self.status = 'Sold'
        print self.status
        return self

    def tax(self, tax):
        self.tax = tax
        total = (self.price * self.tax) + self.price
        print "The product is ${} with tax.".format(total)
        return self

    def return_product(self, reason):
        self.reason = reason
        if reason == 'defective':
            self.status = 'Defective'
            self.price = 0
            print "This product was returned because it was {}. It is now ${}.".format(self.reason, self.price)
        elif reason == 'in box':
            self.status = 'For Sale'
            print "This product was returned like new. It is {}.".format(self.status)
        elif reason == 'opened':
            self.status = 'Opened'
            self.price = self.price - (self.price * .2)
            print "This product was returned {}. It is now ${}".format(self.status, self.price)
        return self

    def display_info(self):
        print "Price: ${}".format(self.price)
        print "Product Name: {}".format(self.name)
        print "Weight: {}lbs".format(self.weight)
        print "Brand: {}".format(self.brand)
        print "Cost: ${}".format(self.cost)
        print "Status: {}".format(self.status)
        return self


    xbox = Product(200, 'XBox', 8, 'Microsoft', 150)