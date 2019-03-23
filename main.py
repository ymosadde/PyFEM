
Meshpath = "Mesh/sphere_test.msh"
with open(Meshpath, 'r') as mshFile:
    mshFileName = mshFile.name
    print('[LOG Mesh] File Name: ' + mshFileName)
    mshFile.readline()
    MeshFormat = mshFile.readline()
    print('[LOG Mesh] Format: ' + MeshFormat)
    mshFile.readline()
    mshFile.readline()
    Nnodes = int(mshFile.readline())
    print('[LOG Mesh] Number of Nodes =  ' + str(Nnodes))

    #read each line of nodes 1)number 2)x 3)y 4)z
    NodesLines = []
    for n in range(Nnodes):
        NodesLines.append(mshFile.readline())

    #split the lines to get coordinates
    Node_X = []
    Node_Y = []
    Node_Z = []
    for n in range(Nnodes):
        split = NodesLines[n].split(" ")
        split[-1] = split[-1].strip() # removes the \n in the last element, Node_Z
        Node_X.append(split[1])
        Node_Y.append(split[2])
        Node_Z.append(split[3])
    #print ('Size of Nx = ' + str(len(Node_X)))
    #print ('Size of Ny = ' + str(len(Node_Y)))
    #print ('Size of Nz = ' + str(len(Node_Z)))

    print(Node_Z)







#mshFile.close() #prevents leaking over maximum allowed file descriptor needed only when read explicitly