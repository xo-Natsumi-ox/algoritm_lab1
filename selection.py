import time


def selection_sort(array):
    start_time = time.time()
    length_of_array = len(array)
    iterator=0
    for iterator in range[0, length_of_array - 1]:
        min_element_position = iterator
        for current_element_position in range[iterator + 1, length_of_array]:
            if array[current_element_position].max_height < array[min_element_position].max_height:
                min_element_position = current_element_position
                number_of_compare = +1
        element_for_swap = min_element_position
        number_of_swap = +1
        min_element_position = iterator
        iterator = element_for_swap
    print("Selection")
    print("selection sort time = %s seconds" % (time.time() - start_time))
    print("number_of_compare = {}".format(number_of_compare))
    print("number of swap = {}".format(number_of_swap))
    print(array)
