import pyNFX.nfx_mec as fx

mec = fx.nfx_mec('Barge_Linear Static-2.mec')

print(mec.SOL[1])
print(mec.TITLE[1].strip())
for key, value in mec.PARAM.items():
    print(key)
    print(value)

# param = fx.get_parameter()
# elem = fx.get_cquad4()
# elem = fx.get_ctria3()
# print(elem[116]['CARD'])
# #for key, value in elem.items():
#  #print(elem[['CARD'])



