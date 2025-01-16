class Coords:

    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def __eq__(self, other_coord):
        print("comparing two coords")
        return self.lat == other_coord.lat and self.lon == other_coord.lon

    # def __ne__(self, other_coord):
    #     print("in __ne__")
    #     return self.lat != other_coord.lat or self.lon != other_coord.lon

    def __lt__(self, other_coord):
        print("is less than")
        return self.lat + self.lon < other_coord.lat + self.lon

    def __le__(self, other_coord):
        print("is less or equal than")
        return self.lat + self.lon <= other_coord.lat + self.lon


point_a = Coords(100, -50)
point_b = Coords(100, -50)

# first time
# print(point_a == point_b)  # False
# print(point_a)  # <__main__.Coords object at 0x7157a815f6b0>
# print(point_b)  # <__main__.Coords object at 0x7157a815f680>

# second time
# point_a.lat == point_b.lat

# second time
print(point_a == point_b)
# OUTPUT:
# comparing two coords
# True

# third time
point_c = Coords(100, -50)
point_d = Coords(101, -50)

# if the magic method __ne__ not exists,
# then the class is gonna use __eq__
print(point_c != point_d)
# OUTPUT:
# in __ne__
# True


# fourth time
point_e = Coords(100, -50)
point_f = Coords(10, -5)
print(point_e < point_f)
print(point_e > point_f)
# OUTPUT:
# is less than
# False
# is less than
# True


# fifth time
point_g = Coords(100, -50)
point_h = Coords(100, -50)
print(point_g <= point_h)
print(point_g >= point_h)
# OUTPUT:
# is less or equal than
# True
# is less or equal than
# True
