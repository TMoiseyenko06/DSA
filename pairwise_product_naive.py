def maxPairWise(numbers):
    n = len(numbers)
    product = 0
    for i in range(n):
        for j in range(n):
            if not i == j:
                if product < numbers[i] * numbers[j]:
                    product = numbers[i] * numbers[j]
    return product

if __name__ == '__main__':
    input_numbers = list(map(int, input.split()))
    print(maxPairWise(input_numbers))
