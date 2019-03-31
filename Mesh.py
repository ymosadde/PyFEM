import numpy as np
class Mesh:

    def __init__(self, tets2nodes, current_nodes_pos):

        self.nodes_pos = current_nodes_pos
        self.tets2nodes = tets2nodes

        self.tet_pos = []
        self.tet_vol = []

    def update(self):
        nodes_pos = self.nodes_pos
        tets2nodes = self.tets2nodes
        Ntets = len(tets2nodes)
        Nnodes = len(nodes_pos)

        tet_pos = []
        volume = []

        for t in range(Ntets):
            n1 = int(tets2nodes[t][0])
            n2 = int(tets2nodes[t][1])
            n3 = int(tets2nodes[t][2])
            n4 = int(tets2nodes[t][3])

            # MAKE ARRAY OUT OF LISTS
            n1_arr = np.asarray(nodes_pos[n1 - 1])
            n2_arr = np.asarray(nodes_pos[n2 - 1])
            n3_arr = np.asarray(nodes_pos[n3 - 1])
            n4_arr = np.asarray(nodes_pos[n4 - 1])

            nx_avg = (n1_arr[0] + n2_arr[0] + n3_arr[0] + n4_arr[0])/4
            ny_avg = (n1_arr[1] + n2_arr[1] + n3_arr[1] + n4_arr[1])/4
            nz_avg = (n1_arr[2] + n2_arr[2] + n3_arr[2] + n4_arr[2])/4

            # UPDATE TET POSITION (COM)
            tet_pos.append([nx_avg, ny_avg, nz_avg])

            # UPDATE TET VOLUME
            vec12 = n2_arr - n1_arr  # vec12 = n2 - n1
            vec13 = n3_arr - n1_arr
            vec14 = n4_arr - n1_arr

            AB_crossv_AC = np.cross(vec12, vec13)
            AD_dot_AB_crossv_AC = np.dot(vec14, AB_crossv_AC)
            volume.append(AD_dot_AB_crossv_AC / 6)

        self.tet_pos = tet_pos
        self.tet_vol = volume



