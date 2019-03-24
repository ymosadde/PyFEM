class Gmsh:
    """class to store all necessary data needed from Gmsh file"""

    def __init__(self, file):
        self.path = file

        self.Name = []
        self.Version = []
        self.Nnodes = []
        self.Nodes_X = []
        self.Nodes_Y = []
        self.Nodes_Z = []
        self.Nelms = []
        self.Ntets = []
        self.Tets2Nodes = []

    def get_gmesh_info(self):
        print('Getting Gmsh:')
        # path = gmsh.path
        with open(self.path, 'r') as msh_file:

            # READ NAME
            name = msh_file.name
            # print('[LOG Mesh] File Name: ' + name)

            # READ VERSION
            msh_file.readline()
            version = msh_file.readline()
            # print('[LOG Mesh] Format: ' + version)

            # READ NUMBER OF NODES
            msh_file.readline()
            msh_file.readline()
            Nnodes = int(msh_file.readline())
            # print('[LOG Mesh] Number of Nodes =  ' + str(Nnodes))

            # READ NODES
            NodesLines = []
            for n in range(Nnodes):
                NodesLines.append(msh_file.readline())

            # split the lines to get coordinates
            Node_X = []
            Node_Y = []
            Node_Z = []
            for n in range(Nnodes):
                node_pieces = NodesLines[n].split(" ")
                node_pieces[-1] = node_pieces[-1].strip()  # removes the \n in the last element, Node_Z
                Node_X.append(float(node_pieces[1]))
                Node_Y.append(float(node_pieces[2]))
                Node_Z.append(float(node_pieces[3]))
            # print ('Size of Nx = ' + str(len(Node_X)))
            # print ('Size of Ny = ' + str(len(Node_Y)))
            # print ('Size of Nz = ' + str(len(Node_Z)))
            # print(Node_Z)

            # READ NUMBER OF TOTAL ELEMENTS
            msh_file.readline()
            msh_file.readline()
            Nelms = int(msh_file.readline())
            # print('[LOG Mesh] Total Number of Elements: ' + str(Nelms))

            # READ ELEMENTS
            ElmLines = []
            for n in range(Nelms):
                ElmLines.append(msh_file.readline())

            # split the lines to get type of element
            ElmType = []

            for n in range(Nelms):
                elm_pieces = ElmLines[n].split(" ")
                elm_pieces[-1] = elm_pieces[-1].strip()  # removes the \n in the last element
                ElmType.append(int(elm_pieces[1]))
            # print(ElmType)

            # TO DO: get surfaces!!!

            # get 4node elements
            Ntets = 0
            TetsLines = []
            for n in range(Nelms):
                # print (ElmType[n])
                if ElmType[n] == 4:
                    Ntets += 1
                    TetsLines.append(ElmLines[n])

            # TO DO: Get physical element IDs

            # print('[LOG Mesh] Number of Tets: ' + str(Ntets))

            # Get Nodes of each tets
            tets2nodes = []
            for n in range(Ntets):
                tet_pieces = TetsLines[n].split(" ")
                tet_pieces[-1] = tet_pieces[-1].strip()  # removes the \n in the last node ID
                fournodes = [tet_pieces[5], tet_pieces[6], tet_pieces[7], tet_pieces[8]]
                tets2nodes.append(fournodes)

            # for n in range(Ntets):
            #   print(Tets2Nodes[n])

        # put info in gmsh object
        self.Name = name
        self.Version = version
        self.Nnodes = Nnodes
        self.Nodes_X = Node_X
        self.Nodes_Y = Node_Y
        self.Nodes_Z = Node_Z
        self.Nelms = Nelms
        self.Ntets = Ntets
        self.Tets2Nodes = tets2nodes

    def log (self):
        print('\t'+'File: ' + str(self.Name) + '\t' + 'Gmsh Version: ' + str(self.Version))
        print('\t''Total Elements ' + str(self.Nelms))
        print('\t''Nodes: ' + str(self.Nnodes) + '\t' + 'Tets: ' + str(self.Ntets))
        print('\t''-----------------------')

