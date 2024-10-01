def area_shape(base,height,shape):
    if shape == "triangle":
     return 0.5 * (base * height)
    elif shape == "parrallelogram":
        return base * height
print (area_shape(2,3,"triangle"))
print (area_shape(8,6,"parrallelogram"))
print (area_shape(2.9,1.3,"parrallelogram"))