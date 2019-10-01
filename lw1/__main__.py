from argparse import ArgumentParser


def is_triangle(edges):
    a, b, c = sorted(edges)
    return (a + b >= c) and all(edge > 0 for edge in edges)


def is_equilateral_triangle(edges):
    a, b, c = edges
    return a == b == c


def is_isosceles_triangle(edges):
    a, b, c = sorted(edges)
    return a == b or b == c


def get_triangle_edges():
    parser = ArgumentParser()
    parser.add_argument("edges", type=int, nargs='+')
    try:
        args = parser.parse_args()
        if len(args.edges) is not 3:
            raise ValueError("Should be three integers as a command line arguments")
        return args.edges
    except BaseException:
        raise Exception("Unknown error")


def classify_triangle(edges):
    if not is_triangle(edges):
        raise Exception("Not a triangle")
    elif is_equilateral_triangle(edges):
        return "Equilateral triangle"
    elif is_isosceles_triangle(edges):
        return "Isosceles triangle"
    else:
        return "Usual triangle"


def main():
    try:
        print(classify_triangle(get_triangle_edges()))
    except BaseException as ex:
        print(ex)


if __name__ == "__main__":
    main()
