import Gmsh
import Mesh
#import Tet


file = "Mesh/sphere_test.msh"
gmsh = Gmsh.Gmsh(file)
gmsh.get_gmesh_info()
gmsh.log()

mesh = Mesh.Mesh(gmsh.tets2nodes)
mesh.update_nodes_pos(gmsh.nodes_pos)


mesh.my_tet_pos[10]
'''
tet = Tet.Tet(gmsh)
tet.get_tet_pos()
tet.get_tet_vol()

v = 0
for t in range(gmsh.Ntets):
    v += tet.Volume[t]
#print('total volume ' + str(v))
r = 1
v_theory = 4 / float(3) * 3.14 * r ** 3
#print('theory volume ' + str(v_theory))
# mesh = Mesh.Mesh()

print(tet.get_tet_pos())
#Gmsh.happy()
'''