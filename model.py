import numpy
import scipy.linalg
from pyscf import fci

norb = 10 
ne = [4,2]

h1e = numpy.zeros((norb,norb))
h1e[:] = 1.0
h2e = numpy.zeros((norb,norb,norb,norb))

fcisol = fci.direct_spin1.FCISolver()
fcisol.max_cycle = 300
fcisol.max_space = 300
fcisol.nroots = 3
fcisol.conv_tol = 1.e-16
fcisol.verbose = 10
fci.addons.fix_spin_(fcisol)
efci,civec = fcisol.kernel(h1e,h2e,norb,ne)
print 'efci =',efci

if fcisol.nroots != 1: 
   for i in range(fcisol.nroots):
      vec = civec[i]
      s2,multi=fci.spin_op.spin_square(vec,norb,ne)
      print "ieig=",i," <S2>/(2S+1)/Seff",s2,multi,(multi-1.0)/2.0
   civec = civec[0]
else:
   s2,multi=fci.spin_op.spin_square(civec,norb,ne)
   print "<S2>/(2S+1)",s2,multi
