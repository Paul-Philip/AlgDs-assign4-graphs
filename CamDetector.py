# Author:   Paul-Philip Mosulet
# Date:     24/9-2016
import reading_input
from my_dijkstra_heap import pop
from my_dijkstra_heap import push
from my_dijkstra_heap import update_distance
from operator import itemgetter


def cam_detector(cameras, adjacency_list, start, k):
    """
    Uses Djikstra's algorithm to find and print
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
    while heap:
        for edge in adjacency_list[heap[0][0]]:
            index_in_heap = vertices[edge[0]]
            new_distance = heap[0][1] + edge[1]
            if cameras[edge[0]] == 1:       # camera found!
                red_lights.append((edge[0], new_distance, heap[0][0]))
            elif index_in_heap == -2:       # non discovered vertex
                push(heap, edge[0], new_distance, vertices, heap[0][0])
            elif index_in_heap > 0 and heap[index_in_heap][1] > new_distance:
                # if distance should be updated
                update_distance(heap, edge[0], new_distance, vertices, heap[0][0])
        vertex = pop(heap, vertices)
        finalized.append(vertex)
        vertices[vertex[0]] = -1

    closest_cameras = []
    i = 1
    while k >= i:
        closest_camera = min(red_lights, key=itemgetter(1))
        while closest_camera[0] in closest_cameras:
            red_lights.remove(closest_camera)
            closest_camera = min(red_lights, key=itemgetter(1))
        print "Camera %d" % i, ": %d" % closest_camera[0], \
            "  Distance from your location: %f" % closest_camera[1]
        print "Shortest path:  %s\n" % print_path(closest_camera, finalized)
        closest_cameras.append(closest_camera[0])
        red_lights.remove(closest_camera)
        if not red_lights:
            break
        i += 1


def find_prev(vertex, list):
    for x in list:
        if x[0] == vertex:
            try:
                return x[2]
            except IndexError:
                return -1


def print_path(end, finalized):
    print_list = [end[0], end[2]]
    previous = find_prev(end[2], finalized)
    while previous != -1:
        print_list.append(previous)
        previous = find_prev(previous, finalized)
    n = len(print_list)-1
    path = str(print_list[n])
    n -= 1
    while 0 <= n:
        path += " --> " + str(print_list[n])
        n -= 1

    return path




def main():
    """
    Reads in vertices with red-light cameras and edges without a toll.
    Reads input values start and k.
    Then performs a Dijkstra from the vertex start using my min heap.
    to find the k closest red-light camera.
    :return:
    """
    cameras = reading_input.read_vertices()
    adjacency_list = reading_input.read_edges()
    start, k = reading_input.user_input()

    cam_detector(cameras, adjacency_list, start, k)


if __name__ == '__main__':
    main()
