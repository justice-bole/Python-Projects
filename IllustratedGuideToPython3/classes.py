#Chapter 21 Classes

#21.2 Defining a Class
class Chair: # 1
    ''' A Chair on a chairlift ''' # 2
    max_occupants = 4

    def __init__(self, id):
        self.id = id
        self.count = 0

    def load(self, number):
        self.count += number

    def unload(self, number):
        self.count -= number


#21.6 Private and Protected Classes
class CorrectChair:
    ''' A Chair on a chairlift '''
    max_occupants = 4

    def __init__(self, id):
        self.id = id
        self.count = 0

    def load(self, number):
        new_val = self._check(self.count + number)
        self.count = new_val

    def unload(self, number):
        new_val = self._check(self.count - number)
        self.count = new_val

    def _check(self, number):
        if number < 0 or number > self.max_occupants:
            raise ValueError('Invalid count:{}'.format(number))
        return number


#21.7 Program Modeling Flow
import random
import time
class CorrectChair:
    ''' A Chair on a chairlift '''
    max_occupants = 4
    def __init__(self, id):
        self.id = id
        self.count = 0
    def load(self, number):
        new_val = self._check(self.count + number)
        self.count = new_val
    def unload(self, number):
        new_val = self._check(self.count - number)
        self.count = new_val
    def _check(self, number):
        if number < 0 or number > self.max_occupants:
            raise ValueError('Invalid count:{}'.format(number))
        return number

NUM_CHAIRS = 100

chairs = []
for num in range(1, NUM_CHAIRS + 1):
    chairs.append(CorrectChair(num))

def avg(chairs):
    total = 0
    for c in chairs:
        total += c.count
    return total/len(chairs)

in_use = []
transported = 0
while True:
    # loading
    loading = chairs.pop(0)
    in_use.append(loading)
    in_use[-1].load(random.randint(0, CorrectChair.max_occupants))
    # unloading
    if len(in_use) > NUM_CHAIRS / 2:
        unloading = in_use.pop(0)
        transported += unloading.count
        unloading.unload(unloading.count)
        chairs.append(unloading)
    print('Loading Chair {} Count:{} Avg:{:.2} Total:{}'.format
        (loading.id, loading.count, avg(in_use), transported))
    time.sleep(.25)