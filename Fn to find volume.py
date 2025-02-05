pi=3.14
def vo_sph(r):
    vols=(4/3)*pi*(r**3)
    print("volume of sphere is :",vols)
def vol_cone(R,h):
    volc=(1/3)*pi*(R**2)*h
    print("volume of cone is:",volc)
def vol_cyl(rad,h):
    volcy=pi*(rad**2)*h
    print("volume of cylinder is:",volcy)
            
vo_sph(3)
vol_cone(3,8)
vol_cyl(4,6)
             
