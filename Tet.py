from typing import List, Any, Union

import numpy as np


class Tet:

    def __init__(self, gmsh):

        self.com = []
        self.tets2nodes = gmsh.Tets2Nodes
        self.Ntets = gmsh.Ntets
        self.nod_x = gmsh.Nodes_X
        self.nod_y = gmsh.Nodes_Y
        self.nod_z = gmsh.Nodes_Z

        self.node_pos = gmsh.nodes_pos

        self.Volume = []
        #self.COM = []

    def get_tet_pos(self):
        node_pos = self.node_pos
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

        #self.tet_pos = tet_pos

    def get_tet_vol(self):
        node_pos = self.node_pos
        tets2nodes = self.tets2nodes
        Ntets = len(tets2nodes)

        Volume = []
        for t in range(Ntets):
            n1 = int(tets2nodes[t][0])
            n2 = int(tets2nodes[t][1])
            n3 = int(tets2nodes[t][2])
            n4 = int(tets2nodes[t][3])

            # MAKE ARRAY OUT OF LISTS
            n1_arr = np.asarray(node_pos[n1 - 1])
            n2_arr = np.asarray(node_pos[n2 - 1])
            n3_arr = np.asarray(node_pos[n3 - 1])
            n4_arr = np.asarray(node_pos[n4 - 1])

            # Making vectors AB, AC and AD
            vec12 = n2_arr - n1_arr  # vec12 = n2 - n1
            vec13 = n3_arr - n1_arr
            vec14 = n4_arr - n1_arr

            AB_crossv_AC = np.cross(vec12, vec13)
            AD_dot_AB_crossv_AC = np.dot(vec14, AB_crossv_AC)

            Volume.append(AD_dot_AB_crossv_AC / 6)
        self.Volume = Volume
