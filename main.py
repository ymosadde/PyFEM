import Gmsh

file = "Mesh/sphere_test2.msh"
gmsh = Gmsh.Gmsh(file)
gmsh.get_gmesh_info()
gmsh.log()


