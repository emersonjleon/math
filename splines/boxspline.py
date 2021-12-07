from itertools import chain
from visualize import p, t, Polytriangle, Scene
import random
#import adjacent as adj


zero=p.Poly([0])

def xypol(p0,p1,p2):
    """Let pi=(xi,yi) points in the plane. we return two
    Poly objects with linear polynomials x0pol, x1pol to be used to construct the x0 and x1 coordinates for Polytriangle objects."""

    x0pol=[p0[0],
           p1[0],p2[0]]
    x1pol=[p0[1],
           p1[1],p2[1]]
    return p.Poly(x0pol), p.Poly(x1pol)


def bsplinet(x,y,num,zp):
    """
    Return a Polytriangle object. x,y specify the left-down
    most lattice coordinate, while num==0 indicates the x side, while num==1 indicates the y side. zp is a poly object
    """
    if num==0:
        xp,yp=xypol([x,y],[x+1,y],[x+1,y+1])
    if num==1:
        xp,yp=xypol([x,y],[x+1,y+1],[x,y+1])
    return Polytriangle(xp,zp,yp,(0,1,2))

def adjpol(prevr, adjI=[0,2,5,9],    newposI=[0,1,3,6]):
    """return a poly from random values except in  entries in positions newpos adI from rpv"""
    ans=[random.random() for i in range(10)]
    for i in range(len(newposI)):
        ans[newposI[i]]=prevr[adjI[i]]
    return ans

def finalpol(firstpol, prevpol):
    lastpol=adjpol(prevpol.coef)
    adjI2=[1,3,6]
    newposI2=[2,5,9]
    for i in range(3):
        lastpol[newposI2[i]]=firstpol.coef[adjI2[i]]
    return lastpol
            
def randombspline6poly():
    """ 
    r0
    r1 r2
    r3 r4 r5
    r6 r7 r8 r9
    """
    r=[random.random() for i in range(10)] 
    polyans=[p.Poly(r)]
    for i in range(4):
        newpol=adjpol(polyans[-1].coef)
        polyans.append(p.Poly(newpol))
    finalcoef=finalpol(polyans[0],polyans[-1])
    polyans.append(p.Poly(finalcoef))
    return polyans

def boxPT(polyans):
    xp0,yp0=xypol([0,0],[1,0],[1,1])
    zp0=polyans[0]
    PTans=[Polytriangle(xp0,zp0,yp0,(0,1,2))]
    xp,yp=xypol([0,0],[1,1],[0,1])
    PTans.append(Polytriangle(xp,    polyans[1],yp,(0,1,2)))
    xp,yp=xypol([0,0],[0,1],[-1,0])
    PTans.append(Polytriangle(xp,    polyans[2],yp,(0,1,2)))
    xp,yp=xypol([0,0],[-1,0],[-1,-1])
    PTans.append(Polytriangle(xp,    polyans[3],yp,(0,1,2)))
    xp,yp=xypol([0,0],[-1,-1],[0,-1])
    PTans.append(Polytriangle(xp,    polyans[4],yp,(0,1,2)))
    xp,yp=xypol([0,0],[0,-1],[1,0])
    PTans.append(Polytriangle(xp,    polyans[5],yp,(0,1,2)))
    for i in range(3):
        PTans[2*i].color='orange'
    return PTans

sc=Scene(boxPT(randombspline6poly()))
sc.writehtml()

"""
x0pol=   [3,
          2,2,
          1,2,1,
          0,0,0,0]
rare=    [2,
          4,8,
          7,3,0,
          -4,-1,8,2]
rare2=    [2,
           8,4,
           0,3,7,
           0,0,0,-4]


prare=p.Poly(rare)

prare2=p.Poly(rare2)


pt1=bsplinet(0,0,0,px0pol)
pt1.color='blue'
pt2=bsplinet(0,0,1,prare2)

sc=Scene([pt1,pt2])

sc.writehtml()
"""
