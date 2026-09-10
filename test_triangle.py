from triangle import classify_triangle 

def test_equilateral():
    assert classify_triangle(3, 3, 3) == "Equilateral"

def test_isosceles():
    assert classify_triangle(5, 5, 2) == "Isosceles"

def test_scalene():
    assert classify_triangle(4, 5, 6) == "Scalene"

def test_right_triangle():
    assert classify_triangle(3, 4, 5) == "Scalene and Right Triangle"


def test_right_triangle_different_order():
    assert classify_triangle(5, 3, 4) == "Scalene and Right Triangle"


def test_invalid_triangle():
    assert classify_triangle(1, 2, 10) == "Not a Triangle!"


def test_zero_side():
    assert classify_triangle(0, 4, 5) == "Not a Triangle!"


def test_negative_side():
    assert classify_triangle(-3, 4, 5) == "Not a Triangle!"