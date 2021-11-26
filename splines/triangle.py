import math

def trianglepos(n):
    """ Give two numbers indicating the triangle position of the nth node (row and posinrow)"""
    kf=math.sqrt(2*n+0.25)-0.5
    k=int(kf)
    if kf%1>0.999999999:
        return (k+1,0)
    else:
        return (k,n-k*(k+1)/2)

def dsumcoords(abpair,d):
    (a,b)=abpair
    return (d-a,a-b,b)

def dcoords(n,d):
    """return the coords a0,a1,a2 of the point in pos(n) with a0 + a1 + a2 = d"""
    return dsumcoords(trianglepos(n),d)

def bcoords(n,d):
    """baricentric coords for the point at position n, subdividing the unit triangle in d^2"""
    return (x/float(d) for x in dsumcoords(trianglepos(n),d)) 


def tlen(d):
    """ return the number of int points of a triangle of side d (d+1 int. points on the side) """
    return (d+1)*(d+2)/2


def indexn( a012):
    """inverse function of dcoors, the number n of position [a]"""
    (a0, a1, a2)=a012
    a=a1+a2    
    return int(a*(a+1)/2+a2)

def tlist(d):
    """list with all integer dcoords in a triangle of side d"""
    return [dcoords(n,d) for n in range(tlen(d))]


def printtriangle(func,d):
    """print the results of func(n) in a triangle"""
    row=0
    l=tlen(d)
    finaltext="\n"
    for n in range(l):
        if n==row*(row+1)/2:
            finaltext += "\n"
            row+=1
        finaltext+= "{0}  ".format(func(n,d))
    print(finaltext)
    return finaltext

def printtlist(l,d):
    """print list l in a triangle of side d"""
    row=0
    le=tlen(d)
    finaltext="\n"
    for n in range(le):
        if n==row*(row+1)/2:
            finaltext += "\n"
            row+=1
        finaltext+= "{0}  ".format(l[n])
    print(finaltext)
    return finaltext



def refl01pos(n,d):
    a0,a1,a2= dcoords(n,d)
    return indexn((a1,a0,a2))

def refl01list(pol,d):
    return [pol[refl01pos(n,d)] for n in range(tlen(d))]


def refl02pos(n,d):
    a0,a1,a2= dcoords(n,d)
    return indexn((a2,a1,a0))

def refl02list(pol,d):
    return [pol[refl02pos(n,d)] for n in range(tlen(d))]

def uppertriang(n):
    """return a triplet corresponding to the triangle with upper point n"""
    a,b = trianglepos(n)    
    return (n, n+a+1, n+a+2)

def lowertriang(n):
    """return a triplet corresponding to the triangle under the upper triangle with point n"""
    a,b = trianglepos(n)    
    return (n+a+1, n+a+2,n+a+2+(a+1)+1)



def uppertriangles(d):
    """list with triplets corresponding to upper triangles, for a triangle of side d"""
    return [uppertriang(n) for n in range(tlen(d-1))]
    

def lowertriangles(d):
    """list with triplets corresponding to upper triangles, for a triangle of side d"""
    return [lowertriang(n) for n in range(tlen(d-2))]

def alltriangles(d):
    return uppertriangles(d)+lowertriangles(d)

if __name__=="__main__":
    print("Draw the homogeneous coordinates of a triangle of side d")
    d=int(input("d = "))
    #printtriangle(dcoords,d)
    
    def ntest(n,d):
        return indexn(dcoords(n,d))

    printtriangle(ntest,d)

    print("\n Upper triangles: ", uppertriangles(d))
    print("\n Lower triangles: ", lowertriangles(d))
