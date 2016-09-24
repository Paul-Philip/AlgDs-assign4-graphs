# Author:   Paul-Philip Mosulet
# Date:     24/9-2016


def read_next(vertices_input):
    """
    :return: next index of camera or -1 if no more cameras present.
    """
    camera_index = vertices_input.readline().split(" ")[0]
    if camera_index == '':   # done reading in.
        return -1
    else:
        return int(camera_index)


def read_vertices():
    """
    Reads in red-light cameras from 'vertices.txt' on the form:
    <index> "camera"
    :return: array with vertices marked 1 - camera, 0 - no camera
    """
    vertices_input = open('vertices.txt', 'r')
    current_camera_index = read_next(vertices_input)
    x = 0
    vertices = []
    while x <= 6104:
        if current_camera_index == x:
            vertices.append(1)
            current_camera_index = read_next(vertices_input)
        else:
            vertices.append(0)
        x += 1
    return vertices


def add_edge(vertex_1, vertex_2, weight, adjacency_list):
    """
    Adds the edge to the adjacency list
    """
    adjacency_list[int(vertex_1)].append((int(vertex_2), float(weight)))
    adjacency_list[int(vertex_2)].append((int(vertex_1), float(weight)))


def read_edges():
    """
    Reads the input edges from edges.txt on the format:
    <vertex1> <vertex2> <weight> "TOLL"(optional)

    Where the vertices are in range 0-6104.
    :return: adjacency list representation of the graph.
    """

    edges_input = open('edges.txt', 'r')
    adjacency_list = [[] for x in range(0,6105)]

    for edge in edges_input:
        edge_info = edge.split(" ")
        try:
            edge_info[3]             # Check if there is a TOLL.
        except IndexError:          # !TOLL catch the Index Error insert edge.
            add_edge(edge_info[0], edge_info[1], edge_info[2], adjacency_list)

    return adjacency_list


def user_input():
    start = input("Enter your location: ")
    k = input("Enter k: ")
    return start, k


def main():
    return

if __name__ == '__main__':
    main()