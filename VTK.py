def printVTK(path, step, mesh):

    with open(path + 'step_' +str(step) + '.vtk', 'w') as vtk:
        Nnodes = len(mesh.nodes_pos)
        nodes_pos = mesh.nodes_pos
        Ntets = len(mesh.tets2nodes)

        # HEADER
        vtk.write('# vtk DataFile Version 3.1\n')
        vtk.write('Tetrahedral Mesh Visualization\n')
        vtk.write('ASCII\n')
        vtk.write('DATASET UNSTRUCTURED_GRID\n')
        vtk.write('\n')

        # NODES
        vtk.write('POINTS ' + str(Nnodes) + ' float\n')
        for n in range(0, Nnodes):
            nx = nodes_pos[n][0]
            ny = nodes_pos[n][1]
            nz = nodes_pos[n][2]
            vtk.write(str(nx) + ' ' + str(ny) + ' ' + str(nz) + '\n')
        vtk.write('\n')

        # CELLS
        vtk.write('CELLS ' + str(Ntets) + ' ' + str(5*Ntets) + '\n')
        for t in range(0, Ntets):
            n1 = str(int(mesh.tets2nodes[t][0])-1)
            n2 = str(int(mesh.tets2nodes[t][1])-1)
            n3 = str(int(mesh.tets2nodes[t][2])-1)
            n4 = str(int(mesh.tets2nodes[t][3])-1)
            vtk.write('4 ' + n1 + ' ' + n2 + ' ' + n3 + ' ' + n4 + '\n')
        vtk.write('\n')
        vtk.write('CELL_TYPES ' + str(Ntets) + '\n')
        for t in range(Ntets):
            vtk.write('10\n')

def printVTK_surface():
    #to do
    pass

