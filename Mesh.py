class Mesh:

    def __init__(self, tets2nodes):
        print('Making Initial Mesh from Gmsh:')

        self.nodes_pos = []
        self.tets2nodes = tets2nodes
        
        #self.my_tet_pos = []
        #self.my_tet_vol = []

    def update_nodes_pos(self, current_nodes_pos):
        self.nodes_pos = current_nodes_pos
        
    '''
    def get_tets_pos(self):
        nodes_pos = self.nodes_pos
        print(nodes_pos)
        tets2nodes = self.tets2nodes
        Ntets = len(tets2nodes)

        com_x = []
        com_y = []
        com_z = []
        for t in range(Ntets):
            n1 = int(tets2nodes[t][0])
            n2 = int(tets2nodes[t][1])
            n3 = int(tets2nodes[t][2])
            n4 = int(tets2nodes[t][3])

            nx_avg = (self.nod_x[n1 - 1] + self.nod_x[n2 - 1] + self.nod_x[n3 - 1] + self.nod_x[n4 - 1]) / 4
            ny_avg = (self.nod_y[n1 - 1] + self.nod_y[n2 - 1] + self.nod_y[n3 - 1] + self.nod_y[n4 - 1]) / 4
            nz_avg = (self.nod_z[n1 - 1] + self.nod_z[n2 - 1] + self.nod_z[n3 - 1] + self.nod_z[n4 - 1]) / 4
            com_x.append(nx_avg)
            com_y.append(ny_avg)
            com_z.append(nz_avg)

        tet_pos = com_x, com_y, com_z
        return tet_pos
'''

    def update(self):
        pass
