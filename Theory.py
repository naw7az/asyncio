from random import randint
import time
import asyncio


def odds(start, stop):  # odds is a generator function
    for odd in range(start, stop + 1, 2):
        yield odd

# gen = odds(3, 15)

# print(gen)
# # print(list(gen))  # if we print this here then next(gen) won't work on next line
# print(next(gen))  # next runs the generator untill the yield point
# print(next(gen))  # next tracks where the value is at any time
# print(list(gen))

def main():
    odd_values = [odd for odd in odds(3, 15)]
    return odd_values

# if __name__ == "__main__":
#     print(main())

def random_num(start, stop):
    time.sleep(3)
    return randint(start, stop)

print(random_num(3, 5))






