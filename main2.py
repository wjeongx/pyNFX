import pyNFX.nfx_mec as mec
import pyNFX.nfx_out as out

inp = mec.nfx_mec('NFXD1_Linear Static-2.mec')
res = out.nfx_out('NFXD1_Linear Static-2.out')

elem = inp.get_cquad4()
elem = inp.get_ctria3()
print(elem[116]['CARD'])

#for key, value in elem.items():
 #print(elem[['CARD'])



