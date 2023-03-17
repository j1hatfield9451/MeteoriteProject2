import PySimpleGUI as psgui
import meteorite_data_class

data = open("MeteoriteDataFile.txt", "r")
data.readline()

mass_list = []
year_list = []


def meteor_filter(mass, year):
    print("main function init")
    while True:
        current_line = data.readline()

        # check if finished reading file
        if current_line == "":
            # print("finished reading")
            break

        current_line = current_line.strip()
        line_list = current_line.split('\t')

        # create empty array of 12 Nones
        current_list = [None] * 12
        for i in range(len(line_list) - 1):
            if line_list[i] != "":
                current_list[i] = line_list[i]

        # easier to just make meteor object before checking mass/year and adding to list after?
        current_meteor = meteorite_data_class.MeteorDataEntry(current_list[0],
                                                              current_list[1],
                                                              current_list[2],
                                                              current_list[3],
                                                              current_list[4],
                                                              current_list[5],
                                                              current_list[6],
                                                              current_list[7],
                                                              current_list[8],
                                                              current_list[9],
                                                              current_list[10],
                                                              current_list[11])

        if current_meteor.mass != None and float(current_meteor.mass) > float(mass):
            mass_list.append(current_meteor)

        if current_meteor.year != None and int(current_meteor.year) >= int(year):
            year_list.append(current_meteor)

    print("filtered lists ready")

    mass_file_print()
    year_file_print()

def mass_file_print():
    mass_file = open("mass_filtered_data.txt", "w")

    for i in range(len(mass_list)):
        mass_file.write(meteorite_data_class.data_values_to_tab_sep_string(mass_list[i]))
        mass_file.write("\n")

    mass_file.close()
def year_file_print():
    year_file  = open("year_filtered_data.txt", "w")

    for i in range(len(year_list)):
        year_file.write(meteorite_data_class.data_values_to_tab_sep_string(year_list[i]))
        year_file.write("\n")

    year_file.close()

def console_print():
    name_label = "NAME"
    mass_label = "MASS (g)"
    year_label = "YEAR"
    print(f'{name_label:<24}{mass_label:<24}')
    print("=" * 40)
    for i in range(len(mass_list)):
        currentName = mass_list[i].name
        currentMass = mass_list[i].mass
        print(f'{currentName:<24}{currentMass:<24}')
    print("=" * 40)

    print(f'{name_label:<24}{year_label:<24}')

    for i in range(len(year_list)):
        currentName = year_list[i].name
        currentYear = year_list[i].year
        print(f'{currentName:<24}{currentYear:<24}')


#TODO txt file method
