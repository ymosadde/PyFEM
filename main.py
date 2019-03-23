
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
        Node_X.append(float(split[1]))
        Node_Y.append(float(split[2]))
        Node_Z.append(float(split[3]))
    #print ('Size of Nx = ' + str(len(Node_X)))
    #print ('Size of Ny = ' + str(len(Node_Y)))
    #print ('Size of Nz = ' + str(len(Node_Z)))

    #print(Node_Z)

    mshFile.readline()
    mshFile.readline()
    Nelms = int(mshFile.readline())
    print('[LOG Mesh] Total Number of Elements: ' + str(Nelms))

    ElmLines = []
    for n in range(Nelms):
        ElmLines.append(mshFile.readline())

    # split the lines to get type of element
    ElmType = []

    for n in range(Nelms):
        splitElms = ElmLines[n].split(" ")
        splitElms[-1] = splitElms[-1].strip()  # removes the \n in the last element
        ElmType.append(int(splitElms[1]))

    #print(ElmType)

    #TO DO: get surfaces!!!

    #get 4node elements
    Ntets = 0
    TetsLines = []
    for n in range(Nelms):
        #print (ElmType[n])
        if ElmType[n] == 4:
            Ntets +=1
            TetsLines.append(ElmLines[n])

    #TO DO: Get physical element IDs

    print('[LOG Mesh] Number of Tets: ' + str(Ntets))

    # Get Nodes of each tets
    Tets2Nodes = []
    for n in range(Ntets):
        splitTets = TetsLines[n].split(" ")
        splitTets[-1] = splitTets[-1].strip()  # removes the \n in the last node ID
        fournodes = [splitTets[5], splitTets[6], splitTets[7], splitTets[8]]
        Tets2Nodes.append(fournodes)


    #for n in range(Ntets):
     #   print(Tets2Nodes[n])