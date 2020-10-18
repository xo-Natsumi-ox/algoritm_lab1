import time


class Heapsort:

    def __init__(self):
        self.number_of_compare = 0
        self.number_of_swap = 0

    def compare_two_elements(self, first_element, second_element):
        self.number_of_compare += 1
        if first_element > second_element:
            return True
        else:
            return False

    def heapify(self, heapify_array, length, index):
        largest = index
        left_element = 2 * index
        right_element = 2 * index + 1
        if left_element < length and Heapsort.compare_two_elements(self, heapify_array[index].max_lifring_weight,
                                                                   heapify_array[left_element].max_lifring_weight):
            largest = left_element
            self.number_of_compare += 1
        if right_element < length and Heapsort.compare_two_elements(self, heapify_array[largest].max_lifring_weight,
                                                                    heapify_array[right_element].max_lifring_weight):
            largest = right_element
            self.number_of_compare += 1
        if largest != index:
            self.number_of_swap += 1
            heapify_array[index], heapify_array[largest] = heapify_array[largest], heapify_array[index]
            Heapsort.heapify(self, heapify_array, length, largest)
            self.number_of_compare += 1
        # return heapify_array,number_of_swap,number_of_compare

    def heap_sort(self, plane_list):

        start_time = time.time()
        heap_array = plane_list
        length = len(heap_array)
        for iterator in range(length, -1, -1):
            Heapsort.heapify(self, heap_array, length, iterator)
        for iterator in range(length - 1, 0, -1):
            heap_array[iterator], heap_array[0] = heap_array[0], heap_array[iterator]
            self.number_of_swap += 1
            Heapsort.heapify(self, heap_array, iterator, 0)
        print("**********   Heapsort   **********")
        print("heap sort time = %s seconds" % (time.time() - start_time))
        print("number of compare = {}".format(self.number_of_compare))
        print("number of swap = {}".format(self.number_of_swap))
        return heap_array
