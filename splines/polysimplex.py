import triangle as t
import poly as p


class Polysimplex():
    """Describe a mapping of the standard simplex into R^3 given by three polynomial objects.  
    also incluldes a list v of three numbers as the vertex name for the three corners."""
    def __init__(self, xpoly, ypoly,zpoly, v):
        self.xpoly=xpoly
        self.ypoly=ypoly
        self.zpoly=zpoly
        self.v=v 

    def computenode(self, dl, n):
        """coords of node n, used in allnodes"""
        bari =tuple(t.bcoords(n,dl))
        #print bari        
        return (self.xpoly.eval(bari), self.ypoly.eval(bari), self.zpoly.eval(bari))

    def allnodes(self, dl):
        """Create a simplicial description with side dl nodes on each side, and return a list 
        with the triplets of coordinates of each vertex. The combinatorics is given by upper and 
        lower triangles"""
        return [self.computenode(dl, n) for n in range(t.tlen(dl))]

    def verticesjstext(self, dl):
        vertjstext="            geometry.vertices= [\n"
        for node in self.allnodes(dl):
            vertjstext += "                new THREE.Vector3"+str(node)+",\n"
        return vertjstext[:-2]+"\n            ];"      
        
    def facesjstext(self, dl):
        facejstext="            geometry.faces= ["
        for face in t.uppertriangles(dl):
            facejstext += "                new THREE.Face3"+str(face)+",\n"
        return facejstext[:-2]+"\n            ];"   
   
    ## geometry.vertices= [new THREE.Vector3(2,1,0), new THREE.Vector3(1,3,0), new THREE.Vector3(3,4,0)];
    ## geometry.faces = [new THREE.Face3(0,1,2)];


if __name__=="__main__":
    deg=3 #degree of polynomials
    l= t.tlen(deg)
 
    constpol=[1,3,3,3,6,3,1,3,3,1]
    x0pol=   [1,2,2,1,2,1,0,0,0,0]
    x1pol=   [0,0,1,0,2,2,0,1,2,1]
    x0x1x2=  [0,0,0,0,9,0,0,0,0,0]
    rare=    [2,4,7,3,1,8,9,0,5,6,-1,-3,8,3,-6]


    prare=p.Poly(rare)
    #prare.tprint()    

    d0p=p.dx0(prare)
    d0p.tprint()

    d1p=p.dx1(prare)
    d1p.tprint()

    d2p=p.dx2(prare)
    d2p.tprint()
    print "#########################"

    ps=Polysimplex(d0p,d1p,d2p, (0,1,2) )
    
    dl=30
    ## t.printtlist(ps.allnodes(dl), dl)
    ## print ps.allnodes(dl)
    print ps.verticesjstext(dl)
    print ps.facesjstext(dl)
    

