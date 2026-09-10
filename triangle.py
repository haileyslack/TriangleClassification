def classify_triangle(a, b, c):

    #checking to make sure the number inputs can actually be valid for a triangle
    if a <= 0 or b <= 0 or c <= 0:
        return "Not a Triangle!"

    if a + b <= c or a + c <= b or b + c <= a:
        return "Not a Triangle!"

    #determine which type of triangle it is
    if a==b and b==c:
        triangle_type = "Equilateral"

    elif a==b or a==c or b==c:
        triangle_type = "Isosceles"

    else:
        triangle_type = "Scalene"

    #check for right triangle
    sides = sorted([a, b, c])

    if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
        triangle_type = triangle_type + " and Right Triangle"

    return triangle_type


#manual test
print(classify_triangle(3, 3, 3))
print(classify_triangle(5, 5, 3))
print(classify_triangle(4, 5, 6))
print(classify_triangle(3, 4, 5))
print(classify_triangle(1, 2, 10))