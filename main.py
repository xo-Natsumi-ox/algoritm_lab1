import csv
import pandas as pd

import plane_info
import selection
import heapsort


# list1=["TupolevTu-134", 47000, 11000]
# list2=["TupolevTu-204", 107900, 7200]
# list3=["IlushinIl-62", 280300, 11000]
# list4=["AirbusA310", 164000, 11000]
# list5=["Boeing-737", 52800, 10058]
# list6=["Boeing-777", 242600, 10668]
# frame = pd.DataFrame([list1,list2,list3,list4,list5,list6])
# frame.to_csv('plane.csv',index=False)
def open_csv(csv_file: str):
    with open(csv_file) as file:
        reader = list(csv.reader(file))
    list_of_planes = []
    for line in reader:
        list_of_planes.append(plane_info.Plane(line[0], int(line[1]), int(line[2])))
    return list_of_planes


if __name__ == '__main__':
    plane_list = open_csv("plane.csv")
    for plane in plane_list:
        print(plane)
    print("")
    sorted_selection = selection.selection_sort(plane_list)
    for plane in sorted_selection:
        print(plane)
    print("")
    heapsort = heapsort.Heapsort()
    sorted_heap = heapsort.heap_sort(plane_list)
    for plane in sorted_heap:
        print(plane)
