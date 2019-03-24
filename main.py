import Gmsh
import Mesh
import Tet

file = "Mesh/sphere_test2.msh"
gmsh = Gmsh.Gmsh(file)
gmsh.get_gmesh_info()
gmsh.log()

tet = Tet.Tet(gmsh)
tet.getCOM()
tet.getVolume()

v = 0
for t in range(gmsh.Ntets):
    v += tet.Volume[t]
print('total volume ' + str(v))
r=30
v_theory = (4/3)*3.14*r**3
print('theory volume ' + str(v_theory))
# mesh = Mesh.Mesh()
