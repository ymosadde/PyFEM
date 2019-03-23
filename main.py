import getMSH

Mesh_File = "Mesh/sphere_test.msh"


tet_to_nodes = []
getMSH.getmesh(Mesh_File, tet_to_nodes)

print(tet_to_nodes)

