import random

def get_numbers_ticket(min: int, max: int, quantity:int) -> list:
    try:
        if type(min) != int or type(max) != int or type(quantity) != int:
            raise ValueError('Function arguments must be integer numbers.')
        elif min < 1:
            raise ValueError('Minimum number should be greater than 0.')
        elif max > 1000:
            raise ValueError('Maximum number should be less than 1000.')
        elif min >= max:
            raise ValueError('Minimum number should be less than maximum number.')
        elif quantity > max - min + 1:
            raise ValueError('The quantity argument must be greater than the difference between the maximum and minimum values.')
        else:
            numbers = []
            while(len(numbers) < quantity):
                num = random.randint(min, max)
                if num in numbers:
                    pass
                else:
                    numbers.append(num)
            return sorted(numbers)
    except Exception as e:
        print(e)
        return []

print("Ваші лотерейні числа:", get_numbers_ticket(10, 99, 7))