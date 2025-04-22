def maxPairWise(numbers):
    n = len(numbers)
    index_1 = 0
    for i in range(2,n):
        if numbers[i] > numbers[index_1]:
            index_1 = i
    if index_1 == 1:
        index_2 = 2
    else:
        index_2 = 1
    for i in range(2,n):
        if (numbers[i] != numbers[index_1]) and (numbers[i] > numbers[index_2]):
            index_2 = i
    return numbers[index_1] * numbers[index_2]

if __name__ == '__main__':
    input_numbers = list(map(int, input().split()))
    print(maxPairWise(input_numbers))
