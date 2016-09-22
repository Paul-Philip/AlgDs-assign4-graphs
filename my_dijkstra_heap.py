# Author:   Paul-Philip Mosulet
# Date:     23/9-2016

from math import floor


def get_dist(heap, n):
    if has_child(heap, n):
        return heap[n][1]
    else:
        return None


def compare_bigger(x, y):
    # type: (int, int) -> boolean
    if x is None or y is None:
        return False
    else:
        return x > y


def get_vertex(heap, n):
    return heap[n][0]


def has_child(heap, child):
    return child < len(heap)


def get_left_right(n):
    return n * 2 + 1, n * 2 + 2


def swap(heap, c_position, p_position, vertices):
    heap[c_position], heap[p_position] = heap[p_position], heap[c_position]
    vertices[get_vertex(heap, p_position)] = p_position
    vertices[get_vertex(heap, c_position)] = c_position


def down_heap(heap, vertices):
    n = 0
    left, right = get_left_right(n)
    while compare_bigger(get_dist(heap, n), get_dist(heap, left)) or \
            compare_bigger(get_dist(heap, n), get_dist(heap, right)):
        if has_child(heap, left):
            swap_child = left
            if compare_bigger(get_dist(heap, left), get_dist(heap, right)):
                swap_child = right
            swap(heap, swap_child, n, vertices)
            n = swap_child
            left, right = get_left_right(n)


def up_heap(heap, n, vertices):
    parent = int(floor((n - 1) / 2))
    while get_dist(heap, n) < get_dist(heap, parent):
        swap(heap, n, parent, vertices)
        n = parent
        parent = int(floor(n-1/ 2))


def update_distance(heap, vertex, distance, vertices):
    heap[vertices[vertex]] = (vertex, distance)  # change previous vertex here
    up_heap(heap, vertices[vertex], vertices)


def push(heap, vertex, distance, vertices):
    heap.append((vertex, distance))  # add previous vertex here :P
    n = len(heap)
    vertices[vertex] = n - 1
    if n > 1:
        up_heap(heap, n - 1, vertices)


def pop(heap, vertices):
    popped = heap[0]
    heap[0] = heap[len(heap) - 1]
    heap.pop(len(heap) - 1)
    down_heap(heap, vertices)
    return popped


def main():
    return


if __name__ == '__main__':
    main()
