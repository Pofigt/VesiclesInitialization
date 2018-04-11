from python_packages.functions.forses import *
from python_packages.shapes.segment import *
from python_packages.shapes.variable import *

def fun_points_in_busket(var, walls):
    
    F = var*0
    mass = 1.0 # mass
    betta = 0.1 # friction coefficient    1.0
    
    for i in range(F.N):
        
        # x - coordinate
        F.X[i] = var.vx(i)
        # y - coordinate
        F.X[i + F.N] = var.vy(i)        
        
        (frx, fry) = (0.0, 0.0)       
        '''
        lr = 1.0
        kr = 1.0
        '''  
        for j in range(walls.vertices_number-1):
            segment_current = Segment(walls.vertices[j], walls.vertices[j+1])
            frx_, fry_ = fr(var, i, segment_current, lr = 5.0, kr = 1.0)
            frx = frx + frx_
            fry = fry + fry_   

        (fpx, fpy) = (0.0, 0.0)
        for j in range(F.N):
            if i!=j:
                fpx_, fpy_ = fp(var.x(i), var.y(i),
                                var.x(j), var.y(j),
                                lr = 3.0, kr = 1.0)
                fpx = fpx + fpx_
                fpy = fpy + fpy_      
        
        (force_x, force_y) = (frx + fpx, fry + fpy)
                      
        # x - velocity
        F.X[i + 2*F.N] = (1/mass)*force_x - betta*var.vx(i)
        
        # y - velocity
        F.X[i + 3*F.N] = (1/mass)*force_y - betta*var.vy(i)
        
        #print(F[:])
        
    return F