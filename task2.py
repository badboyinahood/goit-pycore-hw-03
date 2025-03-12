import random

def get_numbers_ticket(min: int, max: int, quantity: int):
    #cases of returning the empty set
    if min < 1 or max > 1000 or min > max or quantity > (max - min + 1):
        return []

    numbers = random.sample(range(min, max + 1), quantity)
    return sorted(numbers)

# Приклад використання
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
