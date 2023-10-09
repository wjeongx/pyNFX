import os

class nfx_mec:
    ELEM = {}
    GRID = {}
    PARAM = {}

    def __init__(self, input_file):
        # self.input_file = input_file
        self.f = open(input_file, 'r') 
        while True:
            line = self.f.readline()
            if line[0:3] == 'SOL':
                self.SOL = line.split()
            elif line[0:5] == 'TITLE':
                self.TITLE = line.split('=')
            elif line[0:5] == 'PARAM':
                parameter = line.split(',')
                nfx_mec.PARAM[parameter[1]] = parameter[2]
            elif line[0:6].strip() == 'GRID':
                nfx_mec.get_grid(line)
            
            elif line[0:6] == 'CQUAD4':
                nfx_mec.get_cquad4(line)
                
            elif line[0:6] == 'CTRIA3':
                nfx_mec.get_ctria3(line)

    def __del__(self):
        self.f.close()
   
    def get_grid(line):
        grd = line.split(',')
        GID = int(grd[1])
        nfx_mec.GRID[GID] = {
        'CP': grd[2],
        'X': grd[3],
        'Y': grd[4],
        'Z': grd[5]
        }        
    
    def get_cquad4(self, line):
        Elems = line.split(',')
        EID = int(Elems[1])
        nfx_mec.ELEM[EID] = {
            'CARD':Elems[0],
            'PID':Elems[2],
            'G1':Elems[3],
            'G2':Elems[4],
            'G3':Elems[5],
            'G4':Elems[6],
            'THETA': Elems[7],
            'ZOFFS': Elems[8]
                }
        line = self.f.readline()
        Elems = line.split(',')
        nfx_mec.ELEM[EID]['TFLAG'] = Elems[3]
        nfx_mec.ELEM[EID]['T1'] = Elems[4]
        nfx_mec.ELEM[EID]['T2'] = Elems[5]
        nfx_mec.ELEM[EID]['T3'] = Elems[6]
        nfx_mec.ELEM[EID]['T4'] = Elems[7]
        

    def get_ctria3(self, line):
        Elems = line.split(',')
        EID = int(Elems[1])
        nfx_mec.ELEM[EID] = {
            'CARD': Elems[0],
            'PID':Elems[2],
            'G1':Elems[3],
            'G2':Elems[4],
            'G3':Elems[5],
            'THETA': Elems[7],
            'ZOFFS': Elems[8]
            }
        
        line = self.f.readline()
        Elems = line.split(',')
        nfx_mec.ELEM[EID]['TFLAG'] = Elems[3]
        nfx_mec.ELEM[EID]['T1'] = Elems[4]
        nfx_mec.ELEM[EID]['T2'] = Elems[5]
        nfx_mec.ELEM[EID]['T3'] = Elems[6]

    def get_cbar(self, line):
        Elems = line.split(',')
        EID = int(Elems[0]),
        nfx_mec.ELEM[EID]={

        }
        line = self.f.readline()
        nfx_mec[EID]['1'] = 1
        line = self.f.readline()
        nfx_mec[EID]['2'] = 2



        
