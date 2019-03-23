
Meshpath = "Mesh/sphere_test.msh"
mshFile = open(Meshpath, 'r')
mshFileName = mshFile.name
print('[LOG]    Reading Mesh File: ' + mshFileName)

print(mshFile.__sizeof__())