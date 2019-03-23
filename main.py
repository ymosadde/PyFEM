
Meshpath = "Mesh/sphere_test.msh"
with open(Meshpath, 'r') as mshFile:
    mshFileName = mshFile.name

print('[LOG]    Reading Mesh File: ' + mshFileName)

print(mshFile.__sizeof__())

#mshFile.close() #prevents leaking over maximum allowed file descriptor needed only when read explicitly