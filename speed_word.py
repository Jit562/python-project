import random as r
from time import *


def mistake(word , useri):
    error = 0
    for i in range(len(word)):
        try:
            if word[i] != useri[i]:
                error = error + 1
        except:
            error = error + 1
    return error

def speed(start, end , user):

    time_delay = end - start

    time_r = round(time_delay, 2)
    speed_time = len(user)/time_r

    return round(speed_time)


world = ["Python is an interpreted", "object-oriented", "high-level programming language with dynamic semantics", "Its high-level built in data structures", "combined with dynamic typing and dynamic"]

res = r.choice(world)

print(res)

print()
print()
print()

start = time()
user = input("Enter word:  ")
end = time()

sp = speed(start, end , user)

print("speed: ", sp, "S")


err = mistake(world , user)

print("error of world:  ", err)

