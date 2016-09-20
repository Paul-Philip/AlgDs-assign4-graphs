#!/usr/bin/env python


def readnext(cameraIndices):
    cameraIndex = cameraIndices.readline().split(" ")[0]
    if cameraIndex == '':
        return -1
    else:
        return int(cameraIndex)


def readVertices():
    cameraIndices = open('vertices.txt', 'r')
    currentCameraIndex = readnext(cameraIndices)
    x = 0
    vertices = []
    while x <= 6104:
        if currentCameraIndex == x:
            vertices.append(1)
            currentCameraIndex = readnext(cameraIndices)
        else:
            vertices.append(0)
        x += 1
    return vertices


def addEdge(vert1, vert2, weight):
    # TODO adding edges for both vertices
    return 0


def readEdges():
    # TODO reading edges
    edges = []
    # To check if "TOLL":
    # try:
    #     edgesInput[3] #the index of "TOLL" text...
    #     no error? aka there is a TOLL aka. don't add to adjacency list.
    # except IndexError:
    #     no TOLL add edge to adjacency list.
    return edges


def main():
    vertices = readVertices()
    edges = readEdges()


if __name__ == '__main__':
    main()
