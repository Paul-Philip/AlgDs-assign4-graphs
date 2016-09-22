# Author:   Paul-Philip Mosulet
# Date:     23/9-2016

import reading_input
from my_dijkstra_heap import pop
from my_dijkstra_heap import push
from my_dijkstra_heap import update_distance


def cam_detector(cameras, adjacency_list, start, k):
    """
    Uses djikstras algorithm to find and print
    the k closest cameras. With out passing through
    any other cameras or tolled roads.
    """
    if cameras[start] == 1:
        print "Oops! Too late to help!!! Please smile for the camera!"
        return
    heap = [(start, 0)]
    finalized = []
    vertices = [-2 for x in range(0, 6105)]
    vertices[start] = 0
    red_lights = []
    while heap != []:
        for edge in adjacency_list[heap[0][0]]:
            index_in_heap = vertices[edge[0]]
            new_distance = heap[0][1] + edge[1]
            if cameras[edge[0]] == 1:       # camera found!
                red_lights.append((edge[0],new_distance))
            elif index_in_heap == -2:       # non discovered vertex
                push(heap, edge[0], new_distance, vertices)
            elif index_in_heap > 0 and heap[index_in_heap][1] > new_distance:
                # if distance should be updated
                update_distance(heap, edge[0], new_distance, vertices)
        vertex = pop(heap, vertices)
        finalized.append(vertex)
        vertices[vertex[0]] = -1

    # TODO make it print the k closest vertices only.
    for x in red_lights:
        print x


def main():
    """
    Reads in vertices with red-light cameras and edges without a toll.
    Reads input values start and k.
    Then performs a dijkstras from the vertice start using my min heap.
    to find the k closest red-light camera.
    :return:
    """
    cameras = reading_input.read_vertices()
    adjacency_list = reading_input.read_edges()
    start, k = reading_input.user_input()

    cam_detector(cameras, adjacency_list, start, k)


if __name__ == '__main__':
    main()
