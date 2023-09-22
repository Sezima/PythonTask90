def find_average(numbers):
    if numbers == []:
        return 0
    elif (sum(numbers)) % len(numbers) == 0:
        return (sum(numbers)) // len(numbers)
    else:
        return (sum(numbers)) / len(numbers)