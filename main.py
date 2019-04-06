import Gmsh
import Mesh
import time
import VTK

t0 = time.time()

file = "Mesh/sphere_test.msh"
gmsh = Gmsh.Gmsh(file)
gmsh.get_gmesh_info()
gmsh.log()
t_gmsh = time.time()

mesh = Mesh.Mesh(gmsh.tets2nodes, gmsh.nodes_pos)
mesh.update()
t_mesh = time.time()

step = 10
vtk_dir = "VTK/"
for s in range(step):
    for n in range(len(mesh.nodes_pos)):
        mesh.nodes_pos[n][2] += -1

    VTK.printVTK(vtk_dir, s, mesh)

print(t_gmsh - t0)
print(t_mesh - t_gmsh)

