import sys
import os


def createOutputDirectoryIfNeeded():
    if not os.path.exists('output-files'):
        os.makedirs('output-files')


def createAdjacencyMatrixFile(adjacencyMatrix, vertexNum, edgeNum, outputPath):
    outputFile = open(outputPath, 'w')

    outputFile.write(f'{vertexNum} {edgeNum}\n')
    for i in range(vertexNum):
        for j in range(vertexNum):
            outputFile.write(f'{adjacencyMatrix[i][j]}')
        outputFile.write('\n')

    outputFile.close()


def createIncidenceMatrixFile(incidenceMatrix, vertexNum, edgeNum, outputPath):
    outputFile = open(outputPath, 'w')

    outputFile.write(f'{vertexNum} {edgeNum}\n')
    for i in range(vertexNum):
        for j in range(edgeNum):
            outputFile.write(f'{incidenceMatrix[i][j]}')
        outputFile.write('\n')

    outputFile.close()


def createAdjacencyListFile(adjacencyList, vertexNum, edgeNum, outputPath):
    outputFile = open(outputPath, 'w')

    outputFile.write(f'{vertexNum} {edgeNum}\n')
    for i in range(vertexNum):
        for j in range(len(adjacencyList[i])):
            if (j != len(adjacencyList[i]) - 1):
                outputFile.write(f'{adjacencyList[i][j]} -> ')
            else:
                outputFile.write(f'{adjacencyList[i][j]}')
        outputFile.write('\n')

    outputFile.close()


def convertEdgeListFileToAdjacencyMatrix(file, vertexNum, edgeNum):
    fileLines = file.readlines()
    adjacencyMatrix = [[0 for col in range(vertexNum)]
                       for row in range(vertexNum)]

    for line in fileLines:
        if line.strip():
            vertex1, vertex2 = map(int, line.split())
            adjacencyMatrix[vertex1 - 1][vertex2 - 1] = 1
            adjacencyMatrix[vertex2 - 1][vertex1 - 1] = 1

    return adjacencyMatrix


def convertIncidenceMatrixToAdjacencyMatrix(file, vertexNum, edgeNum):
    fileLines = file.readlines()
    incidenceMatrix = []
    adjacencyMatrix = [[0 for col in range(vertexNum)]
                       for row in range(vertexNum)]

    # read incidence matrix
    for line in fileLines:
        if line.strip():
            lineStr = line.strip()
            incidenceMatrix.append(list(map(int, lineStr)))

    # convert incidence matrix to adjacency matrix
    for column in range(len(incidenceMatrix[1])):
        vertexIncided = []
        for line in range(len(incidenceMatrix)):
            if incidenceMatrix[line][column] == 1:
                vertexIncided.append(line)
        adjacencyMatrix[vertexIncided[0]][vertexIncided[1]] = 1
        adjacencyMatrix[vertexIncided[1]][vertexIncided[0]] = 1

    return adjacencyMatrix


def readAdjacencyMatrix(file):
    fileLines = file.readlines()
    adjacencyMatrix = []

    for line in fileLines:
        if line.strip():
            lineStr = line.strip()
            adjacencyMatrix.append(list(map(int, lineStr)))

    return adjacencyMatrix


def convertAdjacencyMatrixToIncidenceMatrix(adjacencyMatrix, vertexNum, edgeNum, outputPath):
    incidenceMatrix = [[0 for col in range(edgeNum)]
                       for row in range(vertexNum)]

    # Variable indicating how many edges have been found in the adjacency matrix
    count = 0

    for line in range(vertexNum):
        for col in range(vertexNum):
            if adjacencyMatrix[line][col] == 1:
                incidenceMatrix[line][count] = 1
                incidenceMatrix[col][count] = 1
                # remove duplicate in adjacency matrix to avoid repeated edges in incidence list
                adjacencyMatrix[col][line] = 0
                count += 1

    createIncidenceMatrixFile(incidenceMatrix, vertexNum, edgeNum, outputPath)


def convertAdjacencyMatrixToAdjacencyList(adjacencyMatrix, vertexNum, edgeNum, outputPath):
    adjacencyList = []

    for line in range(vertexNum):
        vertexAdjancencyList = [line + 1]
        for column in range(vertexNum):
            if adjacencyMatrix[line][column] == 1:
                vertexAdjancencyList.append(column + 1)
        adjacencyList.append(vertexAdjancencyList)

    createAdjacencyListFile(adjacencyList, vertexNum, edgeNum, outputPath)


createOutputDirectoryIfNeeded()
filePath = sys.argv[1]
outputPath = sys.argv[1].replace('input-files', 'output-files')

file = open(filePath, 'r')

inputFileFormat, outputFileFormat = map(int, file.readline().split())
vertexNum, edgeNum = map(int, file.readline().split())

# Deal with input type
if inputFileFormat == 1:
    adjacencyMatrix = convertEdgeListFileToAdjacencyMatrix(
        file, vertexNum, edgeNum)
elif inputFileFormat == 2:
    adjacencyMatrix = readAdjacencyMatrix(file)
elif inputFileFormat == 3:
    adjacencyMatrix = convertIncidenceMatrixToAdjacencyMatrix(
        file, vertexNum, edgeNum)
else:
    print('File provided had incorrect formatting')

# Deal with conversion from adjacency matrix to output type
if outputFileFormat == 1:
    createAdjacencyMatrixFile(adjacencyMatrix, vertexNum, edgeNum, outputPath)
elif outputFileFormat == 2:
    convertAdjacencyMatrixToIncidenceMatrix(
        adjacencyMatrix, vertexNum, edgeNum, outputPath)
elif outputFileFormat == 3:
    convertAdjacencyMatrixToAdjacencyList(
        adjacencyMatrix, vertexNum, edgeNum, outputPath)


file.close()
