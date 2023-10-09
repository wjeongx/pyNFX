import os
import pandas as pd

class nfx_mec:
    def __init__(self, mec_file):
        self.lines = []
        with open(mec_file, 'r') as self.f:
            while True:
                line = self.f.readline()
                if line[0] == '$': continue

                if not line:
                    break
                else:
                    self.lines.append(line)
    
    def __del__(self):
        self.f.close()
    
# GRD_NAME = ['GRID','ID','CP','X1','X2','X3','CD','PS','SEID']
    def GRID_lst(self):

        grd_lst = []
        for line in self.lines:
            grid_line = line.split(',')
            if grid_line[0] == 'GRID':
                grd_lst.append(grid_line)
        
        return grd_lst
#'CQUAD4' 'EID' 'PID' 'G1', 'G2', 'G3', 'G4' 'THETA(MCID)' 'ZOFFS'
#        , , 'TFLAG', 'T1', 'T2', 'T3', 'T4'
#CTRIA3 EID PID G1 G2 G3 THETA(MCID), ZOFFS 
#         TFLAG T1 T2 T3
    def lst2D(self):

        list_2d = []
        for line in self.lines:
            line2d = line.split(',')
            if line2d[0] == 'CQUAD4' or line2d[0] == 'CTRIA3':
                list_2d.append(line2d)
        return list_2d

#CBAR EID PID GA GB X1 X2 X3 OFFT 
#     PA PB W1A W2A W3A W1B W2B W3B
#CBEAM EID PID GA GB X1 X2 X3, , ,OFFT/BIT
#      PA PB W1A W2A W3A W1B W2B W3B 
#      SA SB
#CROD EID PID G1 G2
    def lst1D(self):

        list_1d = []
        for line in self.lines:
            line1d = line.split(',')
            if line1d[0] == 'CBAR' or line1d[0] == 'CBEAM' or line1d[0] == 'CROD':
                list_1d.append(line2d)
        return list_1d

    def __del__(self):
        self.f.close()
   
    # def get_sol(self):
    #     input_file = self.input_file

    #     with open(input_file,'r') as f:
    #         while True:
    #             line = f.readline()
    #             if line[0:3] == 'SOL':
    #                 sol_num = line.split()
    #                 print(line[0:3])
    #             elif not line:
    #                 break

    #     return sol_num[1]

    # def get_title(self):
    #     input_file = self.input_file

    #     with open(input_file,'r') as f:
    #         while True:
    #             line = f.readline()
    #             if line[0:5] == 'TITLE':
    #                 title = line.split('=')
    #                 print(line[0:5])
    #             elif not line:
    #                 break

    #     return title[1].strip()
    
    # def get_parameter(self):
    #     input_file = self.input_file

    #     with open(input_file,'r') as f:
    #         while True:
    #             line = f.readline()
    #             if line[0:5] == 'PARAM':
    #                 parameter = line.split(',')
    #                 nfx_mec.PARAM[parameter[1]] = parameter[2]
    #             elif not line:
    #                 break

    #     return nfx_mec.PARAM
    
    # def get_grid(self):
    #     input_file = self.input_file

    #     with open(input_file, 'r') as f:
    #         while True:
    #             line = f.readline()
    #             if line[0:6].strip() == 'GRID':
    #                 grd = line.split(',')
    #                 GID = int(grd[1])
    #                 nfx_mec.GRID[GID] = {
    #                     'CP': grd[2],
    #                     'X': grd[3],
    #                     'Y': grd[4],
    #                     'Z': grd[5]

    #                 }
    #             elif not line:
    #                 break
    #     return nfx_mec.GRID
    
    # def get_cquad4(self):
    #     input_file = self.input_file

    #     with open(input_file, 'r') as f:
    #         while True:
    #             line = f.readline()
    #             if line[0:6] == 'CQUAD4':
    #                 elm = line.split(',')
    #                 EID = int(elm[1])
    #                 nfx_mec.ELEM[EID] = {
    #                     'CARD':elm[0],
    #                     'PID':elm[2],
    #                     'G1':elm[3],
    #                     'G2':elm[4],
    #                     'G3':elm[5],
    #                     'G4':elm[6],
    #                     'THETA': elm[7],
    #                     'ZOFFS': elm[8]
    #                 }
    #                 line = f.readline()
    #                 elm = line.split(',')
    #                 nfx_mec.ELEM[EID]['TFLAG'] = elm[3]
    #                 nfx_mec.ELEM[EID]['T1'] = elm[4]
    #                 nfx_mec.ELEM[EID]['T2'] = elm[5]
    #                 nfx_mec.ELEM[EID]['T3'] = elm[6]
    #                 nfx_mec.ELEM[EID]['T4'] = elm[7]
    #             elif not line:
    #                 break
    #     return nfx_mec.ELEM

    # def get_ctria3(self):
    #     input_file = self.input_file

    #     with open(input_file, 'r') as f:
    #         while True:
    #             line = f.readline()
    #             if line[0:6] == 'CTRIA3':
    #                 elm = line.split(',')
    #                 EID = int(elm[1])
    #                 nfx_mec.ELEM[EID] = {
    #                     'CARD': elm[0],
    #                     'PID':elm[2],
    #                     'G1':elm[3],
    #                     'G2':elm[4],
    #                     'G3':elm[5],
    #                     'THETA': elm[7],
    #                     'ZOFFS': elm[8]
    #                 }
    #                 line = f.readline()
    #                 elm = line.split(',')
    #                 nfx_mec.ELEM[EID]['TFLAG'] = elm[3]
    #                 nfx_mec.ELEM[EID]['T1'] = elm[4]
    #                 nfx_mec.ELEM[EID]['T2'] = elm[5]
    #                 nfx_mec.ELEM[EID]['T3'] = elm[6]
    #             elif not line:
    #                 break
    #     return nfx_mec.ELEM                

        
