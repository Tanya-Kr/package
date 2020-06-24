import math
import operator


def get_triangle_data():
    triangle_data = input("Enter triangle data: ").split(",")
    return [triangle_data[0], triangle_data[1:]]


def triangle_area_calculation(triangle_data):

    triangle_sides = []
    for item in triangle_data:
        triangle_sides.append(float(item.strip()))

    semi_perimeter = (triangle_sides[0]+triangle_sides[1]+triangle_sides[2]) / 2
    triangle_area = pow((semi_perimeter * (semi_perimeter-triangle_sides[0]) * (semi_perimeter-triangle_sides[1]) * (semi_perimeter-triangle_sides[2])), 0.5)

    return triangle_area


triangles_list_dict = {}


def triangles_list(triangle_name, triangle_area):
    triangles_list_dict = {triangle_name: triangle_area}
    return triangles_list_dict


def sort_triangles_by_area(x):
    return sorted(x.items(), key=operator.itemgetter(1))


if __name__ == '__main__':
    flag = True
    while flag:
        triangle_data = get_triangle_data()
        triangles_list_dict[triangle_data[0]] = triangle_area_calculation(triangle_data[1])
        flag = input("Do you want to continue(y/n): ").lower() == ("y" or "yes")

    print(triangles_list_dict)