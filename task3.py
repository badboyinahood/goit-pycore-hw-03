import re

def normalize_phone(phone_number: str) -> str:
    #delete all symbols except numbers and +
    phone_number = re.sub(r'[^\d+]', '', phone_number.strip())

    # if starts with +380 -> no changes
    if phone_number.startswith('+380'):
        return phone_number

    # if starts with 380 -> add +
    if phone_number.startswith('380'):
        return '+' + phone_number
    # if starts with 0 -> add +38
    if phone_number.startswith('0'):
        return '+38' + phone_number

    # if starts with + -> no changes -> not ukr
    if phone_number.startswith('+'):
        return phone_number

    #other cases -> take as ukr with no code and add +38
    return '+38' + phone_number

#Example data
raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)