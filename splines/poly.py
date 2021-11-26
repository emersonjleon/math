import triangle as t
from adj import adjacent

class Poly:
    def __init__(self,pol):
        self.coef=pol
        self.len=len(pol)
        a,b = t.trianglepos(len(pol))
        if  b!= 0: 
            print("Error, polynomial", pol, "have the wrong length size. what is its degree??")
            print(0/0) 
        else:
            self.deg=a-1
            
    def eval(self, v):
        """ Evaluate pol at point v=(x0,x1,x2). pol is a list of length        
            l=t.tlen(deg) representing coeff c(i,j,k) of x0^i*x1^j*x2^k in pol, 
            where i+j+k=deg degree of pol"""
        x0,x1,x2 = v
        total=0   
        exponents= t.tlist(self.deg)
        for k in range(self.len):
            exps=exponents[k]
            total+= self.coef[k]*(x0**exps[0])*(x1**exps[1])*(x2**exps[2])
        return total

    def tprint(self):
        ans=t.printtlist(self.coef,self.deg)
        return ans

    def der(self, i):
        """compute the derivative of poly with respect to xi."""
        if i==0:    
            derfunc=dx0
        elif i==1:
            derfunc=dx1
        elif i==2:
            derfunc=dx2
        return derfunc(self)

    def adj(self, i):
        return adjacent(self, i)

    
def evalpol(pol,v):
    """ Evaluate pol at point v=(x0,x1,x2). pol is a list of length        
        l=t.tlen(deg) representing coeff c(i,j,k) of x0^i*x1^j*x2^k in pol, 
        where i+j+k=deg degree of pol"""
    x0,x1,x2=v
    total=0   
    exponents= t.tlist(3)# put here deg of pol
    for k in range(l):
        exps=exponents[k]
        total+= pol[k]*(x0**exps[0])*(x1**exps[1])*(x2**exps[2])
    return total

def evalpoln(n,d,pol):
    """evaluate pol at baricentric point n with respect to degree deg"""
    return evalpol(pol, t.bcoords(n,d))


def dx0monomial(poly, n):
    """return the coeff of d pol/dx0 at pos n"""
    a,b=trianglepos(n)
    return poly.coef[n]*a
  


def dx0(poly):
    """produces the Poly of the derivative of poly with respect dx0"""
    row=0
    pol=[]
    d=poly.deg
    l=t.tlen(d - 1)
    for n in range(l):
        if n==row*(row+1)/2:
            row+=1
        pol.append( (d+1-row)*poly.coef[n])
        #print n, (d-row)*poly.coef[n]
        
    return Poly(pol)

def dx1(poly):
    """produces the Poly element of the derivative of poly with respect dx0"""
    rpol=t.refl01list(poly.coef , poly.deg)
    der=dx0(Poly(rpol))
    return Poly(t.refl01list(der.coef,der.deg))

def dx2(poly):
    """produces the Poly element of the derivative of poly with respect dx0"""
    rpol=t.refl02list(poly.coef , poly.deg)
    der=dx0(Poly(rpol))
    return Poly(t.refl02list(der.coef,der.deg))




if __name__=="__main__":
    deg=3 #degree of polynomials
    l= t.tlen(deg)
    print( t.tlen(deg))
    print( t.tlen(deg-1))
 
    constpol=[1,3,3,3,6,3,1,3,3,1]
    x0pol=   [1,2,2,1,2,1,0,0,0,0]
    x1pol=   [0,0,1,0,2,2,0,1,2,1]
    x0x1x2=  [0,0,0,0,9,0,0,0,0,0]
    rare=    [2,4,7,3,1,8,9,0,5,6]


    print("Poly and derivatives")

    p=Poly(rare)
    p.tprint()    

    d0p=dx0(p)
    d0p.tprint()

    d1p=dx1(p)
    d1p.tprint()

    d2p=dx2(p)
    d2p.tprint()

    #pol=constpol    
    pol=x0pol

    print("Evaluate Poly at the triangular grid")

    d=10 ## number of points on the side of the triangle to be evaluated

    def func(n,d):
        return evalpoln(n,d,pol)

    t.printtriangle(func,d)

    print("")


