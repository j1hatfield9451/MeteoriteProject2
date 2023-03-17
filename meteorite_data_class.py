class MeteorDataEntry:
    def __init__(self, name, id, nametype, recclass, mass, fall, year, reclat, reclong, GeoLocation, States, Counties):
        self.name = name
        self.id = id
        self.nametype = nametype
        self.recclass = recclass
        self.mass = mass
        self.fall = fall
        self.year = year
        self.reclat = reclat
        self.reclong = reclong
        self.GeoLocation = GeoLocation
        self.States = States
        self.Countries = Counties


def printInfoTest(MeteorDataEntry):
    print(f'{MeteorDataEntry.name}{MeteorDataEntry.mass}')


def data_values_to_tab_sep_string(self):
    return f'{self.name}\t{self.id}\t{self.nametype}\t{self.recclass}\t{self.mass}\t{self.fall}\t{self.year}\t'\
           f'{self.reclat}\t{self.reclong}\t{self.GeoLocation}\t{self.States}\t{self.Countries}'

