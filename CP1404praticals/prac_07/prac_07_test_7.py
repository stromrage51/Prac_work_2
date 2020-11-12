# FACTOR_MILES_TO_KM = 1.60934
#
# def convert_miles_to_km():
#     k = 'km'
#     miles = float(input("Please enter a number:"))
#     km = miles*FACTOR_MILES_TO_KM
#     print(km)
#
#
# convert_miles_to_km()

class Cat:
    def __init__(self, name="", weight=0, height=0, sex="", breed=""):
        """Initialise cat"""
        self.name = name
        self.weight = weight
        self.height = height
        self.sex = sex
        self.breed = breed

    def __str__(self):
        """Return sting"""
        return "Name={}\nweight={}, height={}\nsex={}, ""breed={}"\
            .format(self.name, self.weight, self.height, self.sex, self.breed)
    def __repr__(self):
        """Return sting value"""
        return str(self.name)

    pass


