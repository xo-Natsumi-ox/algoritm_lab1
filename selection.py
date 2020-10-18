import time


def selection_sort(array: list):
    start_time = time.time()
    length_of_array = len(array)
    number_of_compare = 0
    number_of_swap = 0
    for iteration in range(length_of_array - 1):
        min_element_position = iteration
        number_of_compare = number_of_compare + 1
        for current_element_position in range(iteration + 1, length_of_array):
            if array[current_element_position].max_height < array[min_element_position].max_height:
                min_element_position = current_element_position
                number_of_compare = number_of_compare + 1
        if min_element_position != iteration:
            array[iteration], array[min_element_position] = array[min_element_position], array[iteration]
            number_of_swap = number_of_swap + 1
    print("**********   Selection   **********")
    end_time = time.time() - start_time
    print("selection sort time = seconds" + str(end_time))
    print("number of compare = {}".format(number_of_compare))
    print("number of swap = {}".format(number_of_swap))
    return array
