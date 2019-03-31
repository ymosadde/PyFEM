import Gmsh
import Mesh
#import Tet


file = "Mesh/sphere_test.msh"
gmsh = Gmsh.Gmsh(file)
gmsh.get_gmesh_info()
gmsh.log()

mesh = Mesh.Mesh(gmsh.tets2nodes, gmsh.nodes_pos)
mesh.update()


