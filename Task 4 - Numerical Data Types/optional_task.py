import math
side1 = 20
side2 = 15
side3 = 20
s = ((side1+side2+side3)/2)
print("\n",s,"\n")

area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("\n",area,"\n")

def triangle(side1, side2, side3):
    s = ((side1+side2+side3)/2)
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return s, area

triangle(side1, side2, side3)