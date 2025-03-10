import random

def get_numbers_ticket(min: int, max: int, quantity: int):
    #cases of returning the empty set
    if not(1 <= min <= max <= 1000) or not(min <= quantity <= max):
        return []
    #random.sample() automatically  takes unique random numbers
    #range(min, max + 1) because range(start, stop) includes start but doesnt include stop which is max
    return sorted(random.sample(range(min, max + 1), quantity))

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа: ", lottery_numbers)