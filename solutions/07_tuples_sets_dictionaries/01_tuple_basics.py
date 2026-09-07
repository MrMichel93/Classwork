"""Reference solution for the tuple basics exercise."""


def tuple_basics_results():
    """Return the results requested by the tuple basics TODOs."""
    coordinates = (10, 20, 30)
    x, y, z = coordinates
    colors = ("red", "green", "blue", "yellow")
    single = (5,)
    combined = (1, 2) + (3, 4)
    points = ((0, 0), (1, 2), (3, 4))
    return {
        "coordinates": coordinates,
        "first_coordinate": coordinates[0],
        "last_coordinate": coordinates[-1],
        "length": len(coordinates),
        "unpacked": (x, y, z),
        "first_two_colors": colors[:2],
        "red_count": colors.count("red"),
        "blue_index": colors.index("blue"),
        "single": single,
        "combined": combined,
        "second_point_y": points[1][1],
    }


if __name__ == "__main__":
    print(tuple_basics_results())
