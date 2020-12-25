#this class contains information of a single country
class Country:
    def __init__(self, name="", population="", area="", continent=""):
        self.name = name
        self.population = population
        self.area = area
        self.continent = continent

    def getName(self):
        return self.name

    def getPopulation(self):
        return self.population

    def getArea(self):
        return self.area

    def getContinent(self):
        return self.continent

    def setPopulation(self, population):
        self.population = population

    def setArea(self, area):
        self.area = area

    def setContinent(self, continent):
        self.continent = continent

    def __repr__(self):
        return_String = self.name + " (pop: " + self.population + ", size: " + self.area + ") " + "in " + self.continent
        return return_String
