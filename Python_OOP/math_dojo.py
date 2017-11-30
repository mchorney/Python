
class MathDojo(object):
    def __init__(self):
        self.result = 0
    def add(self, *nums):
        for num in nums:
            self.result += num
        return self
    def substract(self, *nums):
        for num in nums:
            self.result -= num
        return self

print MathDojo().add(2).add(2, 5).substract(3, 2).result

class MathDojo2(object):
    def __init__(self):
        self.result = 0
    def add(self, *nums):
        for num in nums:
            if type(num) is list or type(num) is tuple:
                for item in num:
                    self.result += item
            elif type(num) is int:
                self.result += num
        return self
    def subtract(self, *nums):
        for num in nums:
            if type(num) is list or type(num) is tuple:
                for item in num:
                    self.result -= item
            elif type(num) is int:
                self.result -= num
        return self

print MathDojo2().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result