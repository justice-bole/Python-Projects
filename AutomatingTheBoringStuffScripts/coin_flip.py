import random
number_of_streaks = 0
h_streak = 0
t_streak = 0
for experimentNumber in range(10000):
    for flips in range(100):
        coin_toss = random.randint(0, 1)
        if h_streak >= 6 or t_streak >= 6:
            number_of_streaks += 1
        if coin_toss == 0:
            h_streak += 1
            t_streak = 0
        else:
            t_streak +=1
            h_streak = 0

print('Chance of streak: %s%%' % (number_of_streaks / 10000))