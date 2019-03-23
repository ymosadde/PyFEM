
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
    print('[LOG Mesh] Nodes =  ' + str(Nnodes))

    Nodeslist = []

    for n in range(Nnodes):
        Nodeslist.append(mshFile.readline())
    print(Nodeslist[1])



#mshFile.close() #prevents leaking over maximum allowed file descriptor needed only when read explicitly