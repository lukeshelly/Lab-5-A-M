"""
Lab 05 - Regular Polygon

Design:
The RegularPolygon class stores the number of sides, side length,
and coverage type. The calculations are kept inside the class.
This makes the program easier to change later.

Testing:
The program creates 10 random polygons and asks the user for
polygon information. It checks the input so the program does
not crash when incorrect values are entered.
"""

import math
import random


class RegularPolygon:
    """Stores and calculates regular polygon information."""

    NumPolygonsCreated = 0

    def __init__(self, sides, side_length, coverage):
        """Creates a polygon and stores its information."""
        self.sides = sides
        self.side_length = side_length
        self.coverage = coverage

        RegularPolygon.NumPolygonsCreated += 1

    def __repr__(self):
        """Returns basic polygon information."""
        return f"RegularPolygon({self.sides}, {self.side_length})"

    def GetInradius(self):
        """Returns the inradius."""
        return self.side_length / (
            2 * math.tan(math.pi / self.sides)
        )

    def GetCircumRadius(self):
        """Returns the circumradius."""
        return self.side_length / (
            2 * math.sin(math.pi / self.sides)
        )

    def GetInteriorAngle(self):
        """Returns the interior angle."""
        return (self.sides - 2) * 180 / self.sides

    def GetExteriorAngle(self):
        """Returns the exterior angle."""
        return 360 / self.sides

    def GetShapeType(self):
        """Returns the name of the polygon."""
        shapes = {
            3: "Triangle",
            4: "Square",
            5: "Pentagon",
            6: "Hexagon",
            7: "Heptagon",
            8: "Octagon",
            9: "Nonagon",
            10: "Decagon",
            11: "Undecagon",
            12: "Dodecagon",
            13: "Tridecagon",
            14: "Tetradecagon",
            15: "Pentadecagon"
        }

        return shapes.get(self.sides, "Other Polygon")

    def ComputePerimeter(self):
        """Returns the perimeter."""
        return self.sides * self.side_length

    def ComputeArea(self):
        """Returns the area."""
        return (
            self.sides * self.side_length ** 2
            / (4 * math.tan(math.pi / self.sides))
        )

    def DeterminePolygonType(self):
        """Returns the polygon type."""
        return self.GetShapeType()

    def GetPolygonSideLength(self):
        """Returns the side length."""
        return self.side_length

    @classmethod
    def GetNumPolygonsCreated(cls):
        """Returns the number of polygons created."""
        return cls.NumPolygonsCreated

    @classmethod
    def ChangeNumPolygonsCreated(cls, number):
        """Changes the number of polygons created."""
        cls.NumPolygonsCreated = number


def GetCoverageInfo(polygon):
    """Calculates the number of servers and scan time."""

    devices_per_mile = {
        "City": 15,
        "Urban": 12,
        "Rural": 10
    }

    scan_speed = {
        "City": 15,
        "Urban": 12,
        "Rural": 10
    }

    # Find the number of devices
    number_of_servers = (
        polygon.ComputeArea()
        * devices_per_mile[polygon.coverage]
    )

    # Find the scan time
    seconds = (
        number_of_servers
        / scan_speed[polygon.coverage]
    )

    time_to_scan = seconds / 3600

    return number_of_servers, time_to_scan


def PrintPolygon(polygon):
    """Prints the required polygon information."""

    servers, scan_time = GetCoverageInfo(polygon)

    print(
        f"{polygon.sides:<7}"
        f"{polygon.side_length:<9.2f}"
        f"{polygon.ComputeArea():<11.2f}"
        f"{polygon.ComputePerimeter():<12.2f}"
        f"{polygon.GetShapeType():<17}"
        f"{polygon.GetInradius():<11.2f}"
        f"{polygon.GetCircumRadius():<11.2f}"
        f"{polygon.GetInteriorAngle():<12.2f}"
        f"{polygon.GetExteriorAngle():<11.2f}"
        f"{polygon.coverage:<10}"
        f"{servers:<13.2f}"
        f"{scan_time:<10.4f}"
    )


# -------------------------------------------------------
# Checkpoint 1: Create 10 random coverage records
# -------------------------------------------------------

print("\n10 RANDOM COVERAGE RECORDS")
print("=" * 130)

print(
    f"{'Sides':<7}"
    f"{'Length':<9}"
    f"{'Area':<11}"
    f"{'Perimeter':<12}"
    f"{'Shape':<17}"
    f"{'Inradius':<11}"
    f"{'Circum':<11}"
    f"{'Interior':<12}"
    f"{'Exterior':<11}"
    f"{'Coverage':<10}"
    f"{'Servers':<13}"
    f"{'Time':<10}"
)


# Make 10 random polygons
for count in range(10):

    sides = random.randint(3, 20)
    side_length = random.randint(5, 15)
    coverage = random.choice(
        ["City", "Urban", "Rural"]
    )

    polygon = RegularPolygon(
        sides,
        side_length,
        coverage
    )

    PrintPolygon(polygon)


# -------------------------------------------------------
# Checkpoint 2: Get information from the user
# -------------------------------------------------------

print("\nENTER YOUR COVERAGE INFORMATION")


# Get the number of sides
while True:

    try:
        sides = int(
            input("Number of sides (3-20): ")
        )

        if 3 <= sides <= 20:
            break

        print("Please enter a number from 3 to 20.")

    except ValueError:
        print("Please enter a whole number.")


# Get the side length
while True:

    try:
        side_length = float(
            input(
                "Length of each side (5-15 miles): "
            )
        )

        if 5 <= side_length <= 15:
            break

        print("Please enter a number from 5 to 15.")

    except ValueError:
        print("Please enter a number.")


# Get the coverage type
while True:

    coverage = input(
        "Coverage type (City, Urban, Rural): "
    ).title()

    if coverage in ["City", "Urban", "Rural"]:
        break

    print("Please enter City, Urban, or Rural.")


# Create the user's polygon
user_polygon = RegularPolygon(
    sides,
    side_length,
    coverage
)


# -------------------------------------------------------
# Checkpoint 3: Display the user's results
# -------------------------------------------------------

print("\nYOUR COVERAGE RESULTS")
print("=" * 130)

print(
    f"{'Sides':<7}"
    f"{'Length':<9}"
    f"{'Area':<11}"
    f"{'Perimeter':<12}"
    f"{'Shape':<17}"
    f"{'Inradius':<11}"
    f"{'Circum':<11}"
    f"{'Interior':<12}"
    f"{'Exterior':<11}"
    f"{'Coverage':<10}"
    f"{'Servers':<13}"
    f"{'Time':<10}"
)

PrintPolygon(user_polygon)

print(
    "\nTotal Polygons Created:",
    RegularPolygon.GetNumPolygonsCreated()
)