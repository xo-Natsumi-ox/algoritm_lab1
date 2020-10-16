import csv
import selection
import heapsort

class Plane:
    def __init__(self, name="null", max_height=0, max_lifring_weight=0):
        self.name = name
        self.max_height = int(max_height)
        self.max_lifring_weight = int(max_lifring_weight)

    def __str__(self):
        return "name = {}, max_height = {}, max_lifring_weight = '{}'".format(self.name, self.max_height,
                                                                              self.max_lifring_weight)


if __name__ == '__main__':
    with open('plane.csv') as file:
        list_of_planes = []
        reader = csv.reader(file)
        for line in reader:
            list_of_planes.append(Plane(line[0], int(line[1]), int(line[2])))
            print(line)

    #selection.selection_sort(list_of_planes)
    heapsort= heapsort.Heapsort()
    sorted=heapsort.heapsort(line)

