

def readnext(camerasIndices):
    cameraIndex = camerasIndices.readline().split(" ")[0]
    if cameraIndex == '':
        return -1
    else:
        return int(cameraIndex)


def readVertices():
    camerasIndices = open('vertices.txt','r')
    currentCameraIndex = readnext(camerasIndices)
    x = 0
    vertices = []
    while x <= 6104:
        if currentCameraIndex == x:
            vertices.append(1)
            currentCameraIndex = readnext(camerasIndices)
        else:
            vertices.append(0)
        x += 1
    return vertices


def readEdges():
    edges = []
    return edges


def main():
    vertices = readVertices()
    edges = readEdges()

if __name__ == '__main__':
    main()
