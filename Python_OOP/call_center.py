#Call Center
#Every time a call comes in you need a way to track the Call
#Another requirement is to store calls in a queue while callers wait

class Call(object):
    def __init__(self, id, name, number, time, reason):
        self.id = id
        self.name = name
        self.number = number
        self.time = time
        self.reason = reason
    def display(self):
        print "Call Id:", self.id
        print "Caller Name:", self.name
        print "Phone Number:", self.number
        print "Time of Call:", self.time
        print "Reason of Call:", self.reason
        return self

call1 = Call(1, "Jeff", "206-555-5555", 25, "On Demand Not Working")
call1.display()
call2 = Call(2, "Marie", "253-555-5555", 4, "Incorrect Bill")


class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue = 0
    def add(self, call):
        self.calls.append(call)
        self.queue += 1
        return self
    def remove(self):
        self.calls.pop(0)
        self.queue -= 1
        return self
    def display_info(self):
        for each in self.calls:
            print each.name + ": "+ each.number
        print "The queue is", self.queue
        return self

callcenter1 = CallCenter()
callcenter1.add(call1).add(call2).remove().display_info()