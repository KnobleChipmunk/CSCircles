def trianglePerimeter(xA, yA, xB, yB, xC, yC):
    perimeter = distance2D(xA, yA, xB, yB) + distance2D(xB, yB, xC, yC) + distance2D(xC, yC, xA, yA)
    return perimeter
