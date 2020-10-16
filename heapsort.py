import time


class Heapsort:
    def __init__(self):
        self.number_of_compare = 0
        self.number_of_swap = 0
    def heapify(self, heapify_array, lenght, index):
        largest = index
        left_element = 2 * index + 1
        right_element = 2 * index + 2
        if left_element < lenght and heapify_array[index].max_lifring_weight < heapify_array[
            left_element].max_lifring_weight:
            largest = left_element
            self.number_of_swap = +1
        if right_element < lenght and heapify_array[largest].max_lifring_weight < heapify_array[
            right_element].max_lifring_weight:
            largest = right_element
            self.number_of_swap = +1

        if largest != index:
            heapify_array[index], heapify_array[largest] = heapify_array[largest], heapify_array[index]
            Heapsort.heapify(heapify_array, lenght, largest)
            self.number_of_swap = +1
        self.number_of_compare += 3
    def heapsort(self, array):
        start_time = time.time()
        heap_array = array
        length = len(heap_array)
        for_maxheap = length // 2 - 1
        for iterator in range(for_maxheap, -1):
            Heapsort.heapify(heap_array, length, iterator)
            self.number_of_compare = +1
        for iterator in range(length - 1, 0, 1):
            heap_array[iterator], heap_array[0] = heap_array[0], heap_array[iterator]
            self.number_of_swap = +2
            self.number_of_compare = +1

        print("Heapsort")
        print("heap sort time = %s seconds" % (time.time() - start_time))
        print("number_of_compare = {}".format(self.number_of_compare))
        print("number of swap = {}".format(self.number_of_swap))
        print(heap_array)
