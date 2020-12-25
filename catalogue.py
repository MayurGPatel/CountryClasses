from country import Country
#this class contains information of an entire catalogue of countries (of class Country)
class CountryCatalogue:
    def __init__(self, countryFile):
        self.countryCat = []
        file = open(countryFile)
        lines = file.readlines()
        file.close()
        count = 0
        for line in lines:
            attributes = line.split("|")
            if count > 0:
                self.countryCat.append(Country(attributes[0], attributes[2], attributes[3], attributes[1]))
            count += 1

    def findCountry(self, country):
        found = False
        for nation in self.countryCat:
            if str(nation.getName()) == country:
                found = True
                return nation
        if found == False:
            return None

    def setPopulationOfCountry(self, country, population):
       self.findCountry(country).setPopulation(population)

    def setAreaofCountry(self, country, area):
        self.findCountry(country).setArea(area)

    def setContinentOfCountry(self, country, continent):
        self.findCountry(country).setContinent(continent)

    def addCountry(self, countryName, pop, area, cont):
        if self.findCountry(countryName) == None:
            self.countryCat.append(Country(countryName, pop, area, cont))
#outputs the entire catalogue
    def printCountryCatalogue(self):
        for country in self.countryCat:
            print(country.__repr__())
#sorts the catalogue by name
    def sortCatalogue(self):
        names = []
        for country in self.countryCat:
            names.append((str(country.getName()), str(country.getPopulation()), str(country.getArea()), str(country.getContinent())))
        names.sort()
        self.countryCat.clear()
        for country in names:
            self.countryCat.append(Country(country[0], country[1], country[2], country[3]))
#saves catalogue to a file
    def saveCountryCatalogue(self, fname):
        self.sortCatalogue()
        file = open(fname, 'w')
        file.write("Country|Continent|Population|Area\n")
        for country in self.countryCat:
            file.write("{}|{}|{}|{}".format(country.getName(), country.getContinent(), country.getPopulation(), country.getArea()))
        file.close()



