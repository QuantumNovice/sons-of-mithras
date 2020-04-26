import random

class Parameter:
    def __init__(self, value):
        self.value = value

    def update(self):
        pass

class Anger(Parameter):
    def update(self, event):
        if event <= self.value:
            self.value += 0.1

class Logic(Parameter):
    def update(self, event):
        pass


class Human:
    '''
    Data holder class

    '''
    def __init__(self):
        self.anger = Anger(0.1)
        self.logic = Logic(0.3)
        self.parameters = [self.anger, self.logic]


class Space:
    def __init__(self):
        self.species = []

    def react(self, host, entity):
        for param in host.parameters:
            event = random.random()
            param.update(event)

    def interact(self):
        for host in self.species:
            for entity in self.species:
                if entity != host:
                    self.react(host, entity)

h1 = Human()
print(h1.anger.value)
h2 = Human()
print(h2.anger.value)

s = Space()
s.species = [h1, h2]
s.interact()

for i in s.species:
    print(i.anger.value, i.logic.value)
