import os
import nfx_mec as mec

class nfx_out:
    def __init__(self, result_file):
        self.result_file = result_file
        # self.f = open(result_file, 'r')
    
#    def __del__(self):
#        self.f.close()

    def displacement_vector(self):
        result_file = self.result_file
        
        with open(result_file, 'r') as f:
            while True:
                line = f.readline()
                if line.strip() =='D I S P L A C E M E N T   V E C T O R':
                    for i in range(3): 
                        line = f.readline()

                    dv = {}
                    while True:
                        line = f.readline()
                        if line.strip() == '':
                            break

                        GID  = int(line[0:9].strip())
                        dv[GID] = {
                                'CID': int(line[10:20]),          # Coordinate Id
                                'T1': float(line[20:39]),
                                'T2': float(line[39:54]),
                                'T3': float(line[54:69]),
                                'R1': float(line[69:84]),
                                'R2': float(line[84:99]),
                                'R3': float(line[99:114])
                        }

                elif not line:
                    break
            
        return dv

    def load_vector(self):
        result_file = self.result_file

        with open(result_file, 'r') as f:
            while True:
                line = f.readline()
                if line.strip() =='L O A D   V E C T O R':
                    print(line)
                    for i in range(3): 
                        line = f.readline()

                    lv = {}
                    while True:
                        line = f.readline()
                        if line.strip() == '':
                            break

                        GID  = int(line[0:9].strip())
                        lv[GID] = {
                                'CID': int(line[10:20]),          # Coordinate Id
                                'T1': float(line[20:39]),
                                'T2': float(line[39:54]),
                                'T3': float(line[54:69]),
                                'R1': float(line[69:84]),
                                'R2': float(line[84:99]),
                                'R3': float(line[99:114])
                        }

                elif not line:
                    break
                
        return lv

    def spc_force(self):
        result_file = self.result_file

        with open(result_file, 'r') as f:
            while True:
                line = f.readline()
                if line.strip() =='F O R C E S   O F   S I N G L E - P O I N T   C O N S T R A I N T':
                    for i in range(3): 
                        line = f.readline()

                    spcf = {}
                    while True:
                        line = f.readline()
                        if line.strip() == '':
                            break

                        GID  = int(line[0:9].strip())
                        spcf[GID] = {
                                'CID': int(line[10:20]),          # Coordinate Id
                                'T1': float(line[20:39]),
                                'T2': float(line[39:54]),
                                'T3': float(line[54:69]),
                                'R1': float(line[69:84]),
                                'R2': float(line[84:99]),
                                'R3': float(line[99:114])
                        }

                elif not line:
                    break
            
        return spcf

    def shell_element_force(self,ELEM):
        result_file = self.result_file

        with open(result_file, 'r') as f:
            while True:
                line = f.readline()

                if line.strip() =='F O R C E S   I N   S H E L L   E L E M E N T S':
                    for i in range(6):
                        line = f.readline()

                    shell_force = {}
                    while True:
                        line = f.readline()
                        if line.strip() == '':
                            continue

                        EID  = int(line[0:9].strip())
                        if ELEM[EID]['CARD'] == 'CTRI3': k = 3
                        elif  ELEM[EID]['CARD'] == 'CQUAD4': k = 4

                        for cnt in range(k):
                            shell_force[EID] = {
                                    'GID': int(line[10:21]),          # Grid Id
                                    'FXX': float(line[21:37]),
                                    'FYY': float(line[37:51]),
                                    'FXY': float(line[51:65]),
                                    'MXX': float(line[65:80]),
                                    'MYY': float(line[80:94]),
                                    'MXY': float(line[94:118]),
                                    'QXZ': float(line[118:123]),
                                    'QYZ': float(line[123:137])
                            }

                elif not line:
                    break
                
            return shell_force

    def shell_element_stress(self):
        result_file = self.result_file

        with open(result_file, 'r') as f:
            while True:
                line = f.readline()
                if line.strip() =='S T R E S S E S   I N   S H E L L   E L E M E N T S':
                    for i in range(6): 
                        line = f.readline()

                    shell_stress = {}
                    while True:
                        line = f.readline()
                        if line.strip() == '':
                            break

                        EID  = int(line[0:9].strip())
                        shell_stress[EID] = {
                                'GID': int(line[10:21]),          # Grid id
                                'LOC': line[21:33],
                                'SXX': float(line[33:51]),
                                'SYY': float(line[51:65]),
                                'SXY': float(line[65:79]),
                                'ANGLE': float(line[79:89]),
                                'MAJOR': float(line[89:103]),
                                'MINOR': float(line[103:116]),
                                'VON-MISES': float(line[116:132]),
                        }

                elif not line:
                    break
            
        return shell_stress
    
