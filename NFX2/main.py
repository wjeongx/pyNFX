import pyNFX.NFX_Result as NFX

nfx = NFX.NFX_Result('NFXD1_Linear Static-2.out')

# disps = nfx.displacement_vector()
loads = nfx.load_vector()
print('================')
print(loads)
for key, value in loads.items():
    print(key, value)


