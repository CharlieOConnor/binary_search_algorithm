import random

# Create an array and fill it with an assortment of random numbers in a defined range
list_of_numbers = [random.randrange(0, 100) for i in range(0, 30)]
list_of_numbers.sort()

# Define the start and end of the array
start = 0
end = len(list_of_numbers)
steps = 0

# Prompt the user to enter an integer to perform a binary search for
user_number = int(input("Please enter a number between 0-100: "))
print("Original List: {} \n".format(list_of_numbers))

def binary_search_recursive(array, u_number, s_number, e_number):
    # Redefine the new middle value of the array each time the function is recursively called
    global steps
    middle = (s_number + e_number) // 2

    # If the new array is empty, end the search
    if len(array[s_number:e_number]) == 0:
        steps += 1
        print("This number is not in this list")
        return

    # If the user's number is the midpoint, end the search
    if u_number == array[middle]:
        steps += 1
        print("Step {} - New List:".format(steps), "["+str(array[middle])+"]")
        print("Your number has been found! It took {} attempts".format(steps))
        return
    # If the user's number is greater than the midpoint, ignore all values below the midpoint and continue the search
    elif u_number > array[middle]:
        steps += 1
        print("Step {} - New list: {}".format(steps, array[middle+1:e_number]))
        return binary_search_recursive(array, u_number, middle+1, e_number)
    # If the user's number is less than the midpoint, ignore all values above the midpoint and continue the search
    elif u_number < array[middle]:
        steps += 1
        print("Step {} - New list: {}".format(steps, array[s_number:middle-1]))
        return binary_search_recursive(array, u_number, s_number, middle-1)

binary_search_recursive(list_of_numbers, user_number, start, end)







