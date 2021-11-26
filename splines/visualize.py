import triangle as t
import poly as p


class Polytriangle():
    """Describe a mapping of the standard triangle into R^3 given by three polynomial objects.  
    also incluldes a list v of three numbers as the vertex name for the three corners."""
    def __init__(self, xpoly, ypoly,zpoly, v):
        self.xpoly=xpoly
        self.ypoly=ypoly
        self.zpoly=zpoly
        self.v=v 
        self.color="yellow"

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

    def meshjstext(self, dl,name):
        """create a threejs description of  a mesh representing the polytriangle. Here name is a str name for the pt."""
        vertjstext="            var geometry{0} = new THREE.Geometry();\n            geometry{0}.vertices= [\n".format(name)
        for node in self.allnodes(dl):
            vertjstext += "                new THREE.Vector3"+str(node)+",\n"
        str1="\n            ];\n            geometry{0}.faces= geometry.faces\n".format(name)
        str2="            var mesh= new THREE.Mesh( geometry{0},  {1}material);\n            scene.add(mesh);\n\n".format(name,self.color)
        return vertjstext[:-2] + str1 + str2      
        
def facesjstext(dl):
    facejstext="            geometry.faces= [\n"
    for face in t.uppertriangles(dl):
        facejstext += "                new THREE.Face3"+str(face)+",\n"
    return facejstext[:-2]+"\n            ];\n"   




def visualize(polytlist,dl,outputfile="./threejs/visual.html"):
    """creates the text to visualize in three.js a list of polytriangles"""
    text1=open('visual1.txt')
    text2=open('visual2.txt')
    f = open(outputfile, 'w')
    for line in text1:
        f.write(line)
        #inserted text
    f.write(facesjstext(dl))
    for n, polyt in enumerate(polytlist):
        f.write(polyt.meshjstext(dl,str(n)))
        f.write('\r\n')
    for line in text2:
        f.write(line)
    f.close()


    

   
    ## geometry.vertices= [new THREE.Vector3(2,1,0), new THREE.Vector3(1,3,0), new THREE.Vector3(3,4,0)];
    ## geometry.faces = [new THREE.Face3(0,1,2)];


if __name__=="__main__":
    deg=3 #degree of polynomials
    l= t.tlen(deg)
 
    a=3
    e=-6
    x0pol=   [1,2,2,1,2,1,0,0,0,0]
    x1pol=   [0,0,1,0,2,2,0,1,2,1]
    x0x1x2=  [0,0,0,0,9,0,0,0,0,0]
    rare=    [2,4,8,7,3,0,a,-1,e,2]




    prare=p.Poly(rare)
    #prare.tprint()    

    d0p=p.dx0(prare)
    #d0p.tprint()

    d1p=p.dx1(prare)
    #d1p.tprint()

    d2p=p.dx2(prare)
    #d2p.tprint()
    #print("#########################")

    ps=Polytriangle(d1p,d2p,d0p, (0,1,2) )
    ps.color="orange"
    ps2=Polytriangle(d0p,d1p,d2p, (0,1,2) )
    ps2.color="blue"
    ps3=Polytriangle(d2p,d0p,d1p, (0,1,2) )
    
    
    dl=30
    ## t.printtlist(ps.allnodes(dl), dl)
    ## print ps.allnodes(dl)
    ##print ps.meshjstext(dl,"4","orange")
    ##print facesjstext(dl)
    
    constpol=[1,
              3,3,
              3,6,3,
              1,3,3,1]

    c1=1
    c2=-1
    c3=1
    
    bxoct=[1,
           c3,c3,
           c1,c2,c1,
           0,0,0,0]
    byoct=[0,
           c1,0,
           c3,c2,0,
           1,c3,c1,0]
    bzoct=[0,
           0,c1,
           0,c2,c3,
           0,c1,c3,1]
    
    def bpoly(blist):
        """
          Standard change of variables. 
          Construct a Poly object given the Bezier Berenstein coeficients b_alpha=c_alpha/(d choose alpha)
        """
        return p.Poly([blist[i]*constpol[i] for i in range(10)])
    
    #octt=Polytriangle(bpoly(bxoct),bpoly(byoct),bpoly(bzoct),(0,1,2))

    #test.color='blue'
    octb=Polytriangle(bpoly(bxoct),bpoly(byoct),bpoly(bzoct),(0,1,2))
    octb.color='blue'
    
    """
    ####

    observations:
    Here we try to create a smooth octahedron with highly symetric tiles, 
    using only two control variables c1 and c2. initially c3=1

    for 
    c1=1/2; c2=3/4 

    for 
    c1=2; c2=3/4 
    c1=2; c2=-3/4 
    the blue surface presents extreme points for the middle points 
    of the edges, triangles next to there degenerate
    the second one exagerates tensions, first one relaxes

    for 
    c1=1; c2=3/4 
    we get nicely round shapes for the blue surface

    for 
    c1=1; c2=2 
    edges are round but a bit to much, the shape is like a bag, edge slope seems close to fit with adyacent poly

    for 
    c1=1; c2=2 
    feels so good, this is maybe what i was looking for. soft, round and with nice proportions. Unfortunately trying to close the sphere, we see that it is not smooth enough... soo bad...

    next time: use adyacent method and see its coefficients

    """


    
    x0p=   [1,
            3,3,
            3,6,3,
            0,0,0,0]    
    x1p=   [0,
            3,0,
            3,6,0,
            1,3,3,0]    
    x2p=   [0,
            0,-3,
            0,-6,-3,
            0,-3,-3,-1]    

    octy=Polytriangle(p.Poly(x0p),p.Poly(x1p),p.Poly(x2p),(0,1,2))

 



    def negpoly(blist):
        """
        return the negative Poly, taking all coefficients times -1.    
        """
        return p.Poly([blist[i]*(-1) for i in range(10)])

    octor=Polytriangle(p.Poly(x0p),negpoly(x1p),p.Poly(x2p),(0,1,2))
    octor.color="orange"

    
    visualize([octb],dl)
