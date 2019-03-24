import Gmsh

file = "Mesh/sphere_test.msh"
gmsh = Gmsh.Gmsh(file)
gmsh.get_gmesh_info()

print(gmsh.Name)
print(gmsh.Version)
print(gmsh.Nnodes)
print(gmsh.Nelms)
print(gmsh.Ntets)
#print(gmsh.Tets2Nodes[10])
