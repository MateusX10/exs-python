def CalculateArea(leng, wid):
    area = leng * wid
    return area

length = float(input("Length of land: "))
width = float(input("Width of land: "))

LandArea = CalculateArea(length, width)
print(f"The area of a land  {width:.1f}X{length:.1f}  is {LandArea:.1f}m²")

