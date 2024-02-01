# a function that takes a list and a target parameter
# variables we have: start, middle, end, steps
# recursion or while loop to keep splitting the data
# steps is the time it takes, so increment steps at every split
# conditions to track target position

def binary_search(list, element):
    middle = 0
    start = 0
    end = len(list)
    steps = 0

    while (start<=end):
        print("Step", steps, ":", str(list[start:end+1]))

        steps = steps+1
        middle = (start + end) // 2

        if element == list[middle]:
            return middle
        if element < list[middle]:
            end = middle - 1
        if element > list[middle]:
            start = middle + 1

    return -1

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7

binary_search(my_list, target)