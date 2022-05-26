#Chapter 21
#Classes Exercises 1-4 pg 165-166

#1  Imagine you are designing a banking application. What would a customer look like?
#What attributes would she have? What methods would she have?
class Customer:

    def __init__(self, id):
        self.id = id
        self.count = 0

        def deposit(self, number):
            self.count += number

        def withdraw(self, number):
            self.count -= number

# 2 Imagine you are creating a Super Mario game. You need to define a class to represent
# Mario. What would it look like? If you aren’t familiar with Super Mario, use your
# own favorite video or board game to model a player.

class Player:
    max_jump: 10
    min_jump: 1

    def __init__(self, id):
        self.id = id
        self.count = 0

    def increase_velocity(self, number):
        self.count += number

    def decrease_velocity(self, number):
        self.count -= number