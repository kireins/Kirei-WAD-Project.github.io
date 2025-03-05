# make declaration insert the formula here
def count_triangle_area(base, height):
    area = 0.5 * base * height
    return area

# add your base and height
base = float(input("Base: "))
height = float(input("Height: "))

# and then counting process here
triangle_area = count_triangle_area(base, height)

# show result
print(f"Your Triangle area with base of {base} & height of {height} is {triangle_area}")
