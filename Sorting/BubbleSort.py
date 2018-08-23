class BubbleSort:
    ''' This Class is for the sorting purpose '''

    # Bubble sort in python
    # Sorts numbers in ascending order
    str_input = input("Please enter numbers separated by spaces: ")

    # split the string into numbers & create a list of numbers
    numbers = [float(x) for x in str_input.split()]

    count = len(numbers)

    for outer in range(count - 1):  # bubbles each number to the end
        for i in range(count - outer - 1):
            if numbers[i] > numbers[i + 1]:
                # swap numbers!
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]

    print(numbers)





