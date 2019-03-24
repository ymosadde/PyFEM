import get_mesh_info

gmsh_file = "Mesh/sphere_test.msh"




gmsh = get_mesh_info.Gmsh(gmsh_file)
get_mesh_info.get_mesh_info(gmsh)

print(gmsh.Name)
print(gmsh.Version)
print(gmsh.Nnodes)
print(gmsh.Nelms)
print(gmsh.Ntets)
#print(gmsh.Tets2Nodes[10])
