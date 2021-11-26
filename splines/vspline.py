from itertools import chain
from visualize import p, t, Polytrianglevisualize 
import adjacent as adj

x0pol=   [1,2,2,1,2,1,0,0,0,0]
rare=    [2,4,8,7,3,0,-4,-1,8,2]

prare=vis.p.Poly(rare)
d0p=vis.p.dx0(prare)
d1p=vis.p.dx1(prare)
ans=d0p.tprint()
d1p.tprint()



