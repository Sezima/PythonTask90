def divisible_by(numbers, divisor):
    return [i for i in numbers if i % divisor == 0]
divisible_by([1,5,3], 2)