import meteorite_data_class

data = open("MeteoriteDataFile.txt", "r")
data.readline()

massList = []
yearList = []
while True:
    currentLine = data.readline()

    #check if finished reading file
    if currentLine == "":
        #print("finished reading")
        break

    currentLine = currentLine.strip()
    lineList = currentLine.split('\t')

    #create empty array of 12 Nones
    currentList = [None] * 12
    for i in range(len(lineList)-1):
        if lineList[i] != "":
            currentList[i] = lineList[i]

    #easier to just make meteor object before checking mass/year and adding to list after?
    currentMeteor = meteorite_data_class.MeteorDataEntry(currentList[0],
                                                         currentList[1],
                                                         currentList[2],
                                                         currentList[3],
                                                         currentList[4],
                                                         currentList[5],
                                                         currentList[6],
                                                         currentList[7],
                                                         currentList[8],
                                                         currentList[9],
                                                         currentList[10],
                                                         currentList[11])

    #print(currentMeteor.year)
    if currentMeteor.mass != None and float(currentMeteor.mass) > 2900000:
        massList.append(currentMeteor)

    if currentMeteor.year != None and int(currentMeteor.year) >=2013:
        yearList.append(currentMeteor)

nameLabel = "NAME"
massLabel = "MASS (g)"
yearLabel = "YEAR"
print(f'{nameLabel:<24}{massLabel:<24}')
print("="*40)
for i in range(len(massList)):
    currentName=massList[i].name
    currentMass=massList[i].mass
    print(f'{currentName:<24}{currentMass:<24}')
print("="*40)

print(f'{nameLabel:<24}{yearLabel:<24}')

for i in range(len(yearList)):
    currentName=yearList[i].name
    currentYear=yearList[i].year
    print(f'{currentName:<24}{currentYear:<24}')






