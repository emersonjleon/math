import triangle as t
import poly as p
import adjacent as adj
from polysimplex import Polysimplex
import random

deg=3 #degree of polynomials
l= t.tlen(deg)

constpol=[1,3,3,3,6,3,1,3,3,1]
x0pol=   [1,2,2,1,2,1,0,0,0,0]
x1pol=   [0,1,0,2,2,0,1,2,1,0]
x2pol=   [0,0,1,0,2,2,0,1,2,1]

x0x1x2=  [0,0,0,0,9,0,0,0,0,0]
rare=    [2,4,7,3,1,8,9,0,5,6,-1,-3,8,3,-6]

def linearabc(a,b,c):
    return [a*x0pol[i]+b*x1pol[i]+c*x2pol[i] for i in range(10)]   

ps=p.Poly([1,2,2,1,2,1,0,0,0,0])
psmod=p.Poly([1,2,2,1,2,1.1,0,0.2,0,0.3])
x2pol=p.Poly(   [0,0,1,0,2,2,0,1,2,1])

adp=adj.adjacent(ps,2)
adpmod=adj.adjacent(psmod,2)
adx2=adj.adjacent(x2pol,2)

psx=Polysimplex(ps,x2pol,psmod, (0,1,2))
psxad=Polysimplex(adp, adx2, adp, (0,1,3))
psxad2=Polysimplex(adpmod, adx2, adp, (0,1,3))


dl=20
print psx.verticesjstext(dl)
print psx.facesjstext(dl)
print psxad.verticesjstext(dl)
#print psxad2.verticesjstext(dl)




